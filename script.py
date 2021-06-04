from PIL import Image
import matplotlib.pyplot as plt
import numpy as np
import cv2

from scipy.interpolate import UnivariateSpline
from skimage.morphology import *
img = Image.open("dataset/images/images/aggron.png")

plt.imshow(img)
plt.show()

img1 = img.resize((64,64))
plt.imshow(img1)
plt.show()

img1 = img.resize((64,64), resample=Image.BICUBIC)
plt.imshow(img1)
plt.show()

img1 = img.resize((64,64), resample=Image.LANCZOS)
plt.imshow(img1)
plt.show()


def cartoonize(img_rgb):
    numDownSamples = 2  # number of downscaling steps
    numBilateralFilters = 2  # number of bilateral filtering steps

    # -- STEP 1 --
    # # downsample image using Gaussian pyramid
    img_color = img_rgb
    # for _ in range(numDownSamples):
    #     img_color = cv2.pyrDown(img_color)
    # # repeatedly apply small bilateral filter instead of applying
    # # one large filter
    # for _ in range(numBilateralFilters):
    #     img_color = cv2.bilateralFilter(img_color, 9, 9, 7)
    #
    # # upsample image to original size
    # for _ in range(numDownSamples):
    #     img_color = cv2.pyrUp(img_color)
    # # plt.imshow(img_color)
    # plt.show()

    # make sure resulting image has the same dims as original
    img_color = cv2.resize(img_color, img_rgb.shape[:2])

    # -- STEPS 2 and 3 --
    # convert to grayscale and apply median blur
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2GRAY)
    img_blur = cv2.medianBlur(img_gray, 15)
    # plt.imshow(cv2.bitwise_and(cv2.cvtColor(img_blur, cv2.COLOR_GRAY2RGB), img_color))
    # plt.show()

    # -- STEP 4 --
    # detect and enhance edges
    img_edge = cv2.adaptiveThreshold(img_blur, 255,
                                     cv2.ADAPTIVE_THRESH_MEAN_C,
                                     cv2.THRESH_BINARY, 21, 5)
    # plt.imshow(img_edge)
    # plt.show()

    # -- STEP 5 --
    # convert back to color so that it can be bit-ANDed with color image
    img_edge = cv2.cvtColor(img_edge, cv2.COLOR_GRAY2RGB)
    return cv2.bitwise_and(img_color, img_edge)


def pencil(img_rgb):
    """Applies pencil sketch effect to an RGB image
        :param img_rgb: RGB image to be processed
        :returns: Processed RGB image
    """
    img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_RGB2GRAY)
    img_blur = cv2.GaussianBlur(img_gray, (21, 21), 0, 0)
    img_blend = cv2.divide(img_gray, img_blur, scale=256)

    # if available, blend with background canvas
    # if self.canvas is not None:
    #     img_blend = cv2.multiply(img_blend, self.canvas, scale=1. / 256)

    return cv2.cvtColor(img_blend, cv2.COLOR_GRAY2RGB)

# img = cv2.imread("better_images/1_0011.png")
# cartoon = area_closing(img)
# plt.imshow(cartoon)
# plt.show()
# cartoon = cartoonize(cartoon)
# plt.imshow(cartoon)
# plt.show()

import glob
image_list = []
for filename in glob.glob('better_images/*.png'):
    img = cv2.imread(filename)
    img = cartoonize(img)
    name = filename.split('\\')[1]
    print(cv2.imwrite("cartoons/" + name, img))


