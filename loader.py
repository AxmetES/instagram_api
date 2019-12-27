import requests
import os


def download_img(url, directory):
    filename = 'hubble.jpeg'
    response = requests.get(url)
    response.raise_for_status()

    with open(directory + filename, 'wb') as file:
        file.write(response.content)


def path_dir(directory):
    os.makedirs(directory, exist_ok=True)


def get_spacex_api(url):
    respose = requests.get(url, )
    respose.raise_for_status()
    respose_spacex = respose.json()
    return respose_spacex


def get_image_link(response_spacex):
    image_links = response_spacex['links']['flickr_images']
    print('\n'.join(image_links))


def main():
    directory = 'images/'

    url = 'https://www.reddit.com/r/spacex/comments/bjy7p5/rspacex_crs17_recovery_discussion_updates_thread'
    spacex_url = 'https://api.spacexdata.com/v3/launches/latest'

    # path_dir(directory)
    # download_img(url, directory)

    response_spacex = get_spacex_api(spacex_url)

    get_image_link(response_spacex)


if __name__ == '__main__':
    main()
