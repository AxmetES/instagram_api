## Script for working with Hubble api, Space x api, Instagram api.

This project have three scripts, with them you can 
* download hubble images with [Hubble open API](http://hubblesite.org/api/v3/images) 
* download hubble images with  [Space X API](https://api.spacexdata.com/v3/launches/latest) and 
* cut images to prepare them to upload to Instagram
* upload them to Instagram with [instabot](https://github.com/instagrambot/instabot)

## Getting Started

For the project to work, install all necessary packages 

```python
pip install -r requirements.txt
```

## Motivation

The project is an assignment in online courses [Devman](https://dvmn.org/modules/)

## Running
You must create two folder for save downloaded images, call them `image` and `new_images`.

The script is run from the command line, script download images by image id from hubble api.You must add id when start script.
```python
python fitch_hubble_by_id.py [id]
```
The script is run from the command line, script download images collection by hubble api.
```python
python fetch_hubble_by_collection.py 
```
Second script download images by space x api.
```python
python fitch_spacex.py
```
Thirds script cuts square from downloaded images and save сut pictures to `new_images` folder. 
```python
python cut_image.py
```
Last script upload images from `new_images` folder to instagram account.You must indicate your instagram login and password when you run your script.
```python
python upload_to_instagram.py [your login] [your password]
```
## License

You may copy, distribute and modify the software
