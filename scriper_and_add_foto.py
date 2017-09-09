#!/usr/local/bin/python3.6
# coding: utf-8

# Imports
import os, re, urllib.request
from grab import Grab, UploadFile


def scraiping_add():
    # Search link on the foto
    pointer = Grab()
    pointer.setup(timeout=10, connect_timeout=10)
    pointer.go('http://www.photosight.ru/photos/6599649/?from=best')
    response_url_foto = pointer.doc.select('//img[@id = "big_photo"]/@src').text()
    response_text_foto = pointer.doc.select('//img[@id = "big_photo"]/@alt').text()


    # Split on the list
    list_name_foto = re.split(' +', response_text_foto)

    # Create join string
    str_name_foto = (str(list_name_foto[0]) + '\t' + (str(list_name_foto[1])))

    # Translation of the bytes
    bytes_name_foto = str_name_foto.encode('utf-8')

    # Load foto on the PC
    urllib.request.urlretrieve(response_url_foto, 'image.png')

    # Load foto on the Server
    pointer.go('https://ourfoto.herokuapp.com/add_foto/')
    pointer.doc.set_input('name', bytes_name_foto)
    pointer.doc.set_input('image', UploadFile('image.png'))
    pointer.doc.set_input('text', response_text_foto)
    pointer.doc.submit()

    # Delete foto
    os.remove('image.png')

print(scraiping_add())
