import requests
import os


def check_dir(directory):
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


def main():
    spacex_url = 'https://api.spacexdata.com/v3/launches/latest'
    directory = 'images/'
    check_dir(directory)

    response_spacex = get_spacex_api(spacex_url)

    image_links = get_image_link(response_spacex)
    fetch_spacex_last_launch(image_links, directory)


if __name__ == '__main__':
    main()
