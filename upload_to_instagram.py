import os

import argparse
from instabot import Bot
from common_functions import make_dir


def upload_images(dir, bot):
    collection = os.listdir(dir)
    for image_name in collection:
        if image_name.endswith(('.png', '.jpg', '.jpeg')):
            bot.upload_photo(f'{dir}{image_name}', caption='the task')


def get_argparse():
    parser = argparse.ArgumentParser(description='Image ID to download file')
    parser.add_argument('user', type=str, help='instagram user')
    parser.add_argument('password', type=str, metavar='password', help='instagram password')
    args = parser.parse_args()
    return args


def main():
    directory = 'new_images/'
    make_dir(directory)
    args = get_argparse()
    bot = Bot()
    bot.login(username=args.user, password=args.password)
    upload_images(directory, bot)


if __name__ == '__main__':
    main()
