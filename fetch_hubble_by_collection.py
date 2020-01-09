import requests
import os
import argparse


def path_dir(directory):
    os.makedirs(directory, exist_ok=True)


def download_hubble_image(url, params, directory):
    extension = get_file_extension(url)
    filename = f'{params}.{extension}'
    response = requests.get(url, verify=False)
    response.raise_for_status()
    with open(directory + filename, 'wb') as file:
        file.write(response.content)
    print(f'id {params} image downloaded')


def get_collections_urls(params, directory):
    url = f'http://hubblesite.org/api/v3/image/{params}'
    response = requests.get(url=url)
    response_data = response.json()
    hubble_image_urls = [item['file_url'] for item in response_data['image_files']]
    for link in hubble_image_urls:
        if 'http:' not in link:
            link = 'http:' + link
            download_hubble_image(link, params, directory)


def get_file_extension(url):
    lst = url.split('.')
    extension = lst[-1]
    return extension


def get_collection_id(url, params, directory):
    response = requests.get(url=url, params=params)
    response.raise_for_status()
    response_data = response.json()
    images_id = [item['id'] for item in response_data]
    for id in images_id:
        get_collections_urls(id, directory)


def get_argparse():
    parser = argparse.ArgumentParser(description='Hubble images collection')
    parser.add_argument('collection_name', type=str, help='Name of images collection')
    args = parser.parse_args()
    return args


def main():
    # args = get_argparse()
    directory = 'images/'
    path_dir(directory)
    # params_collection_name = {'page': 'all', 'collection_name': f'{args.collection_name}'}
    params_collection_name = {'page': 'all', 'collection_name': 'printshop'}
    hubble_api = f'http://hubblesite.org/api/v3/images'

    get_collection_id(hubble_api, params_collection_name, directory)


if __name__ == '__main__':
    main()