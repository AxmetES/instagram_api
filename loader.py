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
    print(f'id {params} image downloaded')


def get_collections__urls(params, directory):
    url = f'http://hubblesite.org/api/v3/image/{params}'
    response = requests.get(url=url)
    response_data = response.json()
    hubble_image_urls = [item['file_url'] for item in response_data['image_files']]
    for link in hubble_image_urls:
        if 'http:' not in link:
            link = 'http:' + link
            download_hubble_image(link, params, directory)


def get_hubble_image_url(url):
    response = requests.get(url=url)
    response_data = response.json()
    hubble_image_urls = [item['file_url'] for item in response_data['image_files']]

    len_of_list = len(hubble_image_urls)
    last_url = hubble_image_urls[len_of_list - 1]
    if 'https:' not in last_url:
        last_url = 'https:' + last_url
    return last_url


def get_image_extension(url):
    lst = url.split('.')
    extension = lst[-1]
    return extension


def get_collection_id(url, params, directory):
    response = requests.get(url=url, params=params)
    response.raise_for_status()
    response_data = response.json()
    images_id = [item['id'] for item in response_data]
    for item in images_id:
        get_collections__urls(item, directory)


def main():
    # params_image_id = 3
    params_collection_name = {'page': 'all', 'collection_name': 'holiday_cards'}

    # hubble_api_image_id = f'http://hubblesite.org/api/v3/image/{params_image_id}'
    hubble_api = f'http://hubblesite.org/api/v3/images'
    spacex_url = 'https://api.spacexdata.com/v3/launches/latest'
    directory = 'images/'
    path_dir(directory)

    # response_spacex = get_spacex_api(spacex_url)
    #
    # image_links = get_image_link(response_spacex)
    # fetch_spacex_last_launch(image_links, directory)
    #
    # last_url = get_hubble_image_url(hubble_api_image_id)
    # download_hubble_image(last_url, params_image_id, directory)
    get_collection_id(hubble_api, params_collection_name, directory)


if __name__ == '__main__':
    main()
