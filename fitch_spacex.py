import requests
import os


def check_dir(directory):
    os.makedirs(directory, exist_ok=True)


def fetch_spacex(links, directory):
    for image_number, image_url in enumerate(links):
        filename = f'space_x{image_number}.jpeg'
        response = requests.get(image_url)
        response.raise_for_status()

        with open(directory + filename, 'wb') as file:
            file.write(response.content)


def get_spacex_api_last(url, directory):
    respose = requests.get(url=url)
    respose.raise_for_status()
    response_spacex = respose.json()
    image_links = get_image_link(response_spacex)
    return image_links


def get_image_link(response_spacex):
    image_links = response_spacex['links']['flickr_images']
    return image_links


def get_spacex_api_all(url_all, directory):
    links_index = []
    response = requests.get(url=url_all)
    response_all = response.json()
    for item in response_all:
        if item['links']['flickr_images']:
            if len(links_index) < len(item['links']['flickr_images']):
                links_index = item['links']['flickr_images']
    max_links = links_index
    return max_links


def main():
    spacex_url_last = 'https://api.spacexdata.com/v3/launches/latest'
    spacex_url_all = 'https://api.spacexdata.com/v3/launches'
    directory = 'images/'
    check_dir(directory)

    lust_links = get_spacex_api_last(spacex_url_last, directory)
    if lust_links == []:
        all_links = get_spacex_api_all(spacex_url_all, directory)
        fetch_spacex(all_links, directory)
    else:
        fetch_spacex(lust_links, directory)


if __name__ == '__main__':
    main()
