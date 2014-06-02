import cv
import os

os.system('raspistill -o /home/pi/camera_images/test_start.jpg -rot 180 -w 320 -h 280 -t 0')
a=cv.LoadImage('/home/pi/camera_images/test_start.jpg')
#a_rgb=cv.CreateMat(a.height,a.width,cv.CV_8UC3)
#cv.CvtColor(a,a_rgb,cv.CV_BGR2RGB)
cv.SaveImage("/home/pi/camera_images/testrot.jpg",a)

