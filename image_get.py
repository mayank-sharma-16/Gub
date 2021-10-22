import requests
import shutil

def get_image():

    URL = "https://picsum.photos/seed/picsum/200/300"
    response = requests.get(URL, stream=True)

    with open('queued.png', 'wb') as out_file:
        shutil.copyfileobj(response.raw, out_file)

    