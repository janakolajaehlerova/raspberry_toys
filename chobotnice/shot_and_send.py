#!/usr/bin/python3

from time import sleep
from picamera import PiCamera
import requests

camera = PiCamera()
#camera.resolution = (2592, 1944)
camera.resolution = (1024, 768)
camera.drc_strength = 'low'
camera.start_preview()
# Camera warm-up time
sleep(2)
camera.capture('foo.jpg')
camera.stop_preview()

with open('foo.jpg', 'rb') as f:
    r = requests.post('_address to php script on the server_', files={'soubor': f})
