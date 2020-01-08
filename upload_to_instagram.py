import os
import argparse
import re

from instabot import Bot


def get_argparse():
    parser = argparse.ArgumentParser(description="Some description")
    parser.add_argument('user', type=str, help='instagram user')
    parser.add_argument('password', type=str, metavar='password', help='instagram password')
    args = parser.parse_args()
    return args


def upload_images(dir, bot):
    collection = os.listdir(dir)
    for image_name in collection:
        if re.match(r'\b\w+(.jpg|.png|.jpeg)\b', image_name):
            bot.upload_photo(f'{dir}{image_name}', caption='the task')
            print('image was uploaded')


def main():
    dir = 'new_images/'
    args = get_argparse()
    bot = Bot()
    bot.login(username=args.user, password=args.password)
    upload_images(dir, bot)


if __name__ == '__main__':
    main()
