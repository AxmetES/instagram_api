import os
from PIL import Image
import re


def crop_image(dir_old, dir_new):
    collection = sorted(os.listdir(dir_old))
    for file in collection:
        if re.match(r'\b\w+(.jpg|.png|.jpeg)\b', file):
            image = Image.open(f'{dir_old}{file}')
            width = image.width
            height = image.height
            if width > height:
                diff_width = width - height
                diff_width = diff_width / 2
                print(diff_width)
                coordinates = (diff_width, 0, width - diff_width, height)
                cropped_image = image.crop(coordinates)
                cropped_image.save(f'{dir_new}{file}')
            elif height > width:
                diff_height = height - width
                diff_height = diff_height / 2
                coordinates = (0, diff_height, width, height - diff_height)
                cropped_image = image.crop(coordinates)
                cropped_image.save(f'{dir_new}{file}')
            else:
                image.save(f'{dir_new}{file}')


def main():
    dir_old = 'images/'
    dir_new = 'new_images/'
    crop_image(dir_old, dir_new)


if __name__ == '__main__':
    main()
