import io
import random
import picamera # sudo apt-get install python-picamera
import numpy as np
import cv2
import time

def write_now():
    # Randomly return True (like a fake motion detection routine)
    return random.randint(0, 2) == 0

stream = io.BytesIO()

with picamera.PiCamera() as camera:
    #stream = picamera.PiCameraCircularIO(camera, seconds=20)
    
    #camera.start_recording(stream, format='h264') 
    #count=0
    #record=True

	camera.start_preview()
	time.sleep(2)
	camera.capture(stream, format='jpeg')
	data = np.fromstring(stream.getvalue(), dtype=np.uint8)
	image = cv2.imdecode(data,1)
	cv2.imwrite("test_before.jpg", image);
	gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
	edges = cv2.Canny(gray,50,150,apertureSize = 3)
	cv2.imwrite("test_gray.jpg",gray)
	minLineLength = 100
	maxLineGap = 10
	
	#lines = cv2.HoughLinesP(edges,1,np.pi/180,100,minLineLength,maxLineGap)
	#for x1,y1,x2,y2 in lines[0]:
	#	cv2.line(image,(x1,y1),(x2,y2),(0,255,0),2)
	
	lines = cv2.HoughLines(edges,1,np.pi/180,200)
	for rho,theta in lines[0]:
		a = np.cos(theta)
		b = np.sin(theta)
#		print 180-theta*180/np.pi
		x0 = a*rho
		y0 = b*rho
		x1 = int(x0 + 1000*(-b))
		y1 = int(y0 + 1000*(a))
		x2 = int(x0 - 1000*(-b))
		y2 = int(y0 - 1000*(a))

		cv2.line(image,(x1,y1),(x2,y2),(0,0,255),2)
		#break
	cv2.imwrite('test_lines.jpg',image) 

	img = cv2.imread('test_before.jpg')
	gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
	edges = cv2.Canny(gray,50,150,apertureSize = 3)
	minLineLength = 100
	maxLineGap = 10
	lines = cv2.HoughLinesP(edges,1,np.pi/180,100,minLineLength,maxLineGap)
	for x1,y1,x2,y2 in lines[0]:
	    cv2.line(img,(x1,y1),(x2,y2),(0,255,0),2)
	cv2.imwrite('test_lines2.jpg',img) 
