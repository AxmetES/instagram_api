import os


def make_dir(directory):
    os.makedirs(directory, exist_ok=True)


def get_file_extension(url):
    file_name, extension = os.path.splitext(url)
    return extension



