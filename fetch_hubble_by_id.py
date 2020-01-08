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


def get_hubble_image_url(url):
    response = requests.get(url=url)
    response_data = response.json()
    hubble_image_urls = [item['file_url'] for item in response_data['image_files']]

    len_of_list = len(hubble_image_urls)
    last_url = hubble_image_urls[len_of_list - 1]
    if 'https:' not in last_url:
        last_url = 'https:' + last_url
    return last_url


def get_file_extension(url):
    lst = url.split('.')
    extension = lst[-1]
    return extension


def get_argparse():
    parser = argparse.ArgumentParser(description='Image ID to download file')
    parser.add_argument('id', type=int, help='image id')
    args = parser.parse_args()
    return args


def main():
    args = get_argparse()

    params_image_id = args.id

    hubble_api_image_id = f'http://hubblesite.org/api/v3/image/{params_image_id}'
    directory = 'images/'
    path_dir(directory)

    last_url = get_hubble_image_url(hubble_api_image_id)
    download_hubble_image(last_url, params_image_id, directory)


if __name__ == '__main__':
    main()
