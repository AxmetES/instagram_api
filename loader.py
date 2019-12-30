import requests
import os
import pprint
import json
import urllib.parse
from urllib.parse import urlparse


def path_dir(directory):
    os.makedirs(directory, exist_ok=True)


def fetch_spacex_last_launch(links, directory):
    for image_number, image_url in enumerate(links):
        filename = f'hubble{image_number}.jpeg'
        response = requests.get(image_url)
        response.raise_for_status()

        with open(directory + filename, 'wb') as file:
            file.write(response.content)


def get_spacex_api(url):
    respose = requests.get(url)
    respose.raise_for_status()
    respose_spacex = respose.json()
    return respose_spacex


def get_image_link(response_spacex):
    image_links = response_spacex['links']['flickr_images']
    return image_links


def download_hubble_image(url, params, directory):
    extension = get_image_extension(url)
    filename = f'{params}.{extension}'

    response = requests.get(url, verify=False)
    response.raise_for_status()
    with open(directory + filename, 'wb') as file:
        file.write(response.content)


def get_hubble_image_url(url):
    response = requests.get(url=url)
    response_hubble = response.json()
    hubble_image_urls = [item['file_url'] for item in response_hubble['image_files']]

    lenth_of_list = len(hubble_image_urls)
    last_url = hubble_image_urls[lenth_of_list - 1]
    if 'https:' not in last_url:
        last_url = 'https:' + last_url
    return last_url


def get_image_extension(url):
    lst = url.split('.')
    extension = lst[-1]
    return extension


def main():
    hubble_params = 1
    hubble_api = f'http://hubblesite.org/api/v3/image/{hubble_params}'
    spacex_url = 'https://api.spacexdata.com/v3/launches/latest'
    directory = 'images/'
    path_dir(directory)
    # str = '//imgsrc.hubblesite.org/hvi/uploads/image_file/image_attachment/1/full_jpg.jpg'

    # response_spacex = get_spacex_api(spacex_url)
    #
    # image_links = get_image_link(response_spacex)
    # fetch_spacex_last_launch(image_links, directory)

    last_url = get_hubble_image_url(hubble_api)
    download_hubble_image(last_url, hubble_params, directory)


if __name__ == '__main__':
    main()
