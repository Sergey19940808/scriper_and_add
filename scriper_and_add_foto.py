#!/usr/local/bin/python3.6
# coding: utf-8

# Imports
import os
import urllib.request

from grab import Grab, UploadFile


def scraiping_add():
    # Search link on the foto
    pointer = Grab()
    pointer.setup(timeout=25, connect_timeout=25)
    pointer.go('http://www.photosight.ru/photos/6599649/?from=best')
    response_url_foto = pointer.doc.select('//img[@id = "big_photo"]/@src').text()
    response_text_foto = pointer.doc.select('//img[@id = "big_photo"]/@alt').text()

    # Load foto on the PC
    urllib.request.urlretrieve(response_url_foto, 'image.png')

    # Load foto on the Server
    pointer.go('https://ourfoto.herokuapp.com/add_foto/')
    pointer.doc.set_input('image', UploadFile('image.png'))
    pointer.doc.set_input('text', response_text_foto)
    pointer.doc.submit()

    # Delete foto
    os.remove('image.png')


print(scraiping_add())
