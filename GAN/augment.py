import glob
from PIL import Image
import numpy as np
import PIL
image_list = []
for filename in glob.glob('dataset/images/images/*.png'):
    img = Image.open(filename)
    img = img.convert("RGBA")
    img = np.array(img)
    flipped = np.flip(img)
    flipped_up = np.flip(img, axis=0)
    flipped_side = np.flip(img, axis=1)
    flipped_color = np.flip(img, axis=2)
    noise = np.random.randint(-1, 2, size=img.shape)
    noisy = img + noise
    noisy = np.clip(noisy, 0, 255).astype("uint8")
    name = filename.split('\\')[-1]

    flipped = Image.fromarray(flipped)
    flipped_up = Image.fromarray(flipped_up)
    flipped_side = Image.fromarray(flipped_side)
    flipped_color = Image.fromarray(flipped_color)
    noisy = Image.fromarray(noisy)

    flipped.save("dataset/images/augment/flipped_"+name)
    flipped_up.save("dataset/images/augment/flipped_up_"+name)
    flipped_side.save("dataset/images/augment/flipped_side_"+name)
    flipped_color.save("dataset/images/augment/flipped_color_"+name)
    noisy.save("dataset/images/augment/noisy_"+name)
    print("Saved: ", name)


