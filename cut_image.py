import os
from PIL import Image


def crop_image(dir_old, dir_new):
    collection = sorted(os.listdir(dir_old))
    for file_name in collection:
        if file_name.endswith(('.png', '.jpg', '.jpeg')):
            image = Image.open(f'{dir_old}{file_name}')
            width = image.width
            height = image.height
            if width > height:
                diff_width = width - height
                diff_width = diff_width / 2
                coordinates = (diff_width, 0, width - diff_width, height)
                cropped_image = image.crop(coordinates)
                cropped_image.save(f'{dir_new}{file_name}')
            elif height > width:
                diff_height = height - width
                diff_height = diff_height / 2
                coordinates = (0, diff_height, width, height - diff_height)
                cropped_image = image.crop(coordinates)
                cropped_image.save(f'{dir_new}{file_name}')
            else:
                image.save(f'{dir_new}{file_name}')


def main():
    dir_old = 'images/'
    dir_new = 'new_images/'
    crop_image(dir_old, dir_new)


if __name__ == '__main__':
    main()
