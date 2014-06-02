#from SimpleCV import *
#from operator import add

import time

#cam = Camera()

#display=Display()     # essential addition


 

normaldisplay = True
 
import SimpleCV
 
cam = SimpleCV.Camera()
display = SimpleCV.Display()
time.sleep(5)     # essential addition MAC
normaldisplay = True

while display.isNotDone():
 
#	try:
		img = cam.getImage().flipHorizontal()
		###
		lines = img.findLines()
		corners = img.findCorners()
		for line in lines:
			if abs(line.angle()) > 45:
				meanColor = line.meanColor()
				print meanColor
				line.draw(SimpleCV.Color.RED) #outline the line segments in red
		
		#left_side_corners = corners.filter(corners.x() < img.width / 2)
		#only look at corners on the left half of the image
		
		longest_line = lines.sortLength()[0]
		#get the longest line returned
		####
		
	
		if normaldisplay:
			img.show()
		else:
			segmented.show()
#	except:
#		print "error?"



 
