from SimpleCV import *
import time

cam = Camera()

dis=Display()     # essential addition
time.sleep(5)     # essential addition

while True:
    img = cam.getImage()
    img.show()
