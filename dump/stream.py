import io
import random
import picamera
import numpy as np
import cv2


def parse_video(stream):
    print('Writing video!')
    # Find the first header frame in the video
    camera.capture(stream, format='jpeg')
    data = np.fromstring(stream.getvalue(), dtype=np.uint8)
    res = cv2.resize(data,None,fx=2,fy=2,interpolation=cv2.INTER_CUBIC)
    
    #print res
    #print 'showed?'
    #gbr to rgb conversion is not working...
    #image = image[:, :, ::-1]
    #print image

with picamera.PiCamera() as camera:
    stream = picamera.PiCameraCircularIO(camera, seconds=5)
    camera.start_recording(stream, format='h264')
    try:
        while True:
            camera.wait_recording(1)
            # Keep recording for 10 seconds and only then write the
            # stream to disk
            parse_video(stream)
    finally:
        camera.stop_recording()
