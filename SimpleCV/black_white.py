from SimpleCV import * #Camera
import time

# Initialize the camera
cam = Camera()
dis = Display()
time.sleep(5)
# Loop to continuously get images
while True:
    # Get Image from camera
    img = cam.getImage()
    # Make image black and white
    img = img.binarize()
    # Draw the text "Hello World" on image
    img.drawText("Hello World!")
    # Show the image
    img.show()
