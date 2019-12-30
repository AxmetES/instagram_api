import requests
import os
import pprint


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


def get_hubble_image(url, params):
    response = requests.get(url=url, params=params)
    response_hubble = response.json()['image_files']
    for item in response_hubble:
        print(item.get('file_url'))


def main():
    params_hubble = {' ': 1}
    hubble_api = 'http://hubblesite.org/api/v3/image/1'
    spacex_url = 'https://api.spacexdata.com/v3/launches/latest'
    directory = 'images/'
    path_dir(directory)

    # response_spacex = get_spacex_api(spacex_url)
    #
    # image_links = get_image_link(response_spacex)

    # print(image_links)

    # fetch_spacex_last_launch(image_links, directory)

    get_hubble_image(hubble_api, params_hubble)


if __name__ == '__main__':
    main()
