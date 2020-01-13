import os
import requests
from dotenv import load_dotenv
from common_functions import make_dir
import datetime
import pprint


def get_image(url_image, directory):
    url, file_name = os.path.split(url_image)
    response = requests.get(url_image, verify=False)
    response.raise_for_status()
    with open(directory + file_name, 'wb') as file:
        file.write(response.content)


def get_nasa_api(url, params, directory):
    response = requests.get(url=url, params=params)
    response_nasa = response.json()
    for item in response_nasa:
        get_image(item['url'], directory)


def main():
    load_dotenv(verbose=True)
    api_key = os.getenv('API_KEY')
    directory = 'images/'

    first_date = '2019-11-5'
    second_date = '2019-11-10'

    format_str = '%Y-%m-%d'
    start_date = datetime.datetime.strptime(first_date, format_str)
    end_date = datetime.datetime.strptime(second_date, format_str)
    start_date = start_date.date().isoformat()
    end_date = end_date.date().isoformat()
    print(start_date)
    print(end_date)

    params = {'api_key': f'{api_key}', 'start_date': start_date, 'end_date': end_date}
    url = 'https://api.nasa.gov/planetary/apod'

    make_dir(directory)
    get_nasa_api(url, params, directory)


if __name__ == '__main__':
    main()
