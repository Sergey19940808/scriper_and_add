#!/usr/local/bin/python3.6
# coding: utf-8

# Imports
import urllib.request
from grab import Grab, UploadFile



# Function for load and upload foto
def load_and_upload_foto():
    # Search link on the foto
    pointer = Grab()
    pointer.go('http://www.photosight.ru/photos/6599649/?from=best')
    response_url_foto = pointer.doc.select('//img[@id="big_photo"]/@src').text()

    if (response_url_foto != None):
        # Load foto on the PC
        urllib.request.urlretrieve(response_url_foto, 'image.png')
    else:
        print('Не удалось получить данные')


    # Load foto on the Server
    pointer.go('http://learning_logs/add_foto')
    pointer.set_input('name', 'fly')
    pointer.set_input('image', UploadFile('image.png'))
    pointer.set_input('text', 'Это очень маленькая и гибкая птичка')
    pointer.submit()











