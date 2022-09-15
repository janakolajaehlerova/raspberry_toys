#!/usr/bin/python3

from time import sleep
from picamera import PiCamera
import requests
import datetime

camera = PiCamera()
camera.resolution = (2592, 1944)
camera.drc_strength = 'low'
camera.start_preview()
print("Camera warm-up time")
sleep(2)
try:
    while True:
         filename = "/home/kam/photos/" + datetime.datetime.now().strftime("%y%m%d_%H%M%S") + ".jpg"
         print(filename)
         camera.capture(filename)
#         sleep(1)
except KeyboardInterrupt:
    pass
camera.stop_preview()

