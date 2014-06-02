import io
import time
import picamera
import cv2
import numpy as np


def read_from_camera():
	# Construct a numpy array from the stream
	print 1
	data = np.fromstring(stream.getvalue(), dtype=np.uint8)
	print 2
	# "Decode" the image from the array, preserving colour
	img = cv2.imdecode(data, 1)
	
	gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	edges = cv2.Canny(gray,50,150,apertureSize = 3)


	minLineLength = 100
	maxLineGap = 10

	#lines = cv2.HoughLinesP(edges,1,np.pi/180,100,minLineLength,maxLineGap)
	
	lines = cv2.HoughLines(edges,1,np.pi/180,200)

	print (lines)

	if lines != None:

		for rho,theta in lines[0]:
		    a = np.cos(theta)
		    b = np.sin(theta)
		    x0 = a*rho
		    y0 = b*rho
		    x1 = int(x0 + 1000*(-b))
		    y1 = int(y0 + 1000*(a))
		    x2 = int(x0 - 1000*(-b))
		    y2 = int(y0 - 1000*(a))
		
		    cv2.line(img,(x1,y1),(x2,y2),(0,0,255),2)
		
		cv2.imwrite('houghlines3.jpg',img)

while True:
	# Create the in-memory stream
	stream = io.BytesIO()

	with picamera.PiCamera() as camera:
    		camera.start_preview()
    		camera.capture(stream, format='jpeg')
		#try:
		read_from_camera()
		#except:
		#print ("no lines")
