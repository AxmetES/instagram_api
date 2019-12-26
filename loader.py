import requests
import os


def download_img(url, filename):
    response = requests.get(url)
    response.raise_for_status()

    with open(filename, 'wb') as file:
        file.write(response.content)


def path_dir(directory):
    os.makedirs(directory, exist_ok=True)


def main():
    directory = 'images'
    filename = 'images\hubble.jpeg'
    url = 'https://upload.wikimedia.org/wikipedia/commons/3/3f/HST-SM4.jpeg'

    path_dir(directory)
    download_img(url, filename)


if __name__ == '__main__':
    main()
