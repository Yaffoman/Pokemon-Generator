#!/usr/bin/env python3
import os
import sys
import numpy as np
import random
from keras import models
from keras import optimizers
from keras.layers.normalization import BatchNormalization
from keras.layers.convolutional import Conv2D, Conv2DTranspose, UpSampling2D
from keras.layers.pooling import MaxPooling2D
from keras.layers.core import Dense, Activation, Flatten, Reshape, Dropout
from keras.layers import Input
from keras.optimizers import Adam, Adagrad, Adadelta, Adamax, SGD
from keras.callbacks import CSVLogger
from keras.layers.advanced_activations import LeakyReLU
import scipy
import h5py
from args import Args
from data import denormalize4gan


def build_enc(shape):
    return build_discriminator(shape, build_disc=False)


def build_discriminator(shape, build_disc=True):
    '''
    Build discriminator.
    Set build_disc=False to build an encoder network to test
    the encoding/discrimination capability with autoencoder...
    '''

    def conv2d(x, filters, shape=(4, 4), **kwargs):
        '''
        I don't want to write lengthy parameters so I made a short hand function.
        '''
        x = Conv2D(filters, shape, strides=(2, 2),
                   padding='same',
                   kernel_initializer=Args.kernel_initializer,
                   **kwargs)(x)
        x = BatchNormalization(momentum=Args.bn_momentum)(x)
        x = LeakyReLU(alpha=Args.alpha_D)(x)
        return x

    face = Input(shape=shape)
    x = face

    # Warning: Don't batchnorm the first set of Conv2D.
    x = Conv2D(64, (4, 4), strides=(2, 2),
               padding='same',
               kernel_initializer=Args.kernel_initializer)(x)
    x = LeakyReLU(alpha=Args.alpha_D)(x)
    # 32x32
    x = conv2d(x, 64)
    x = conv2d(x, 128)
    # 16x16

    x = conv2d(x, 256)
    # 8x8

    x = conv2d(x, 512)
    # 4x4

    if build_disc:
        x = Flatten()(x)

        # 1 when "real", 0 when "fake".
        x = Dense(1, activation='sigmoid',
                  kernel_initializer=Args.kernel_initializer)(x)
        return models.Model(inputs=face, outputs=x)
    else:
        # build encoder.
        x = Conv2D(Args.noise_shape[2], (4, 4), activation='tanh')(x)
        return models.Model(inputs=face, outputs=x)


def build_gen(shape):
    def deconv2d(x, filters, shape=(4, 4)):
        '''
        Conv2DTransposed gives me checkerboard artifact...
        Select one of the 3.
        '''
        # Simpe Conv2DTranspose
        # Not good, compared to upsample + conv2d below.
        x = Conv2DTranspose(filters, shape, padding='same',
                            strides=(2, 2), kernel_initializer=Args.kernel_initializer)(x)

        x = BatchNormalization(momentum=Args.bn_momentum)(x)
        x = LeakyReLU(alpha=Args.alpha_G)(x)
        return x

    noise = Input(shape=Args.noise_shape)
    x = noise
    # 1x1x256
    # noise is not useful for generating images.

    x = Conv2DTranspose(512, (4, 4),
                        kernel_initializer=Args.kernel_initializer)(x)
    x = BatchNormalization(momentum=Args.bn_momentum)(x)
    x = LeakyReLU(alpha=Args.alpha_G)(x)
    # 4x4x512
    x = deconv2d(x, 256)
    # 8x8x256
    x = deconv2d(x, 128)
    # 16x16x128
    x = deconv2d(x, 64)
    # 32x32x64
    x = deconv2d(x, 32)
    # Extra layer
    x = Conv2D(64, (5, 5), padding='same',
               kernel_initializer=Args.kernel_initializer)(x)
    x = BatchNormalization(momentum=Args.bn_momentum)(x)
    x = LeakyReLU(alpha=Args.alpha_G)(x)
    # 32x32x64

    x = Conv2DTranspose(3, (4, 4), padding='same', activation='tanh',
                        strides=(2, 2), kernel_initializer=Args.kernel_initializer)(x)
    # 64x64x3

    return models.Model(inputs=noise, outputs=x)
