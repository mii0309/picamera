import cv2  
import picamera.array
import picamera
import numpy as np

cascade_file="cascade.xml"
with picamera.PiCamera() as camera:
  with picamera.array.PiRGBArray(camera) as stream:
    camera.resolution=(640,480)
    while True:
      camera.capture(stream,'bgr',use_video_port=True)
      gray = cv2.cvtColor(stream.array, cv2.COLOR_BGR2GRAY)
      cascade=cv2.CascadeClassifier(cascade_file)
      objects=cascade.detectMultiScale(gray, minSize=(640,480))
      for(x,y,w,h) in objects:
        print(x,y,w,h) 
        color = (0, 0, 255)
        pen_w = 5
        cv2.rectangle(stream.array, (x, y), (x+w, y+h), color, thickness = pen_w)
        cv2.imshow('frame',stream.array)
        
      if cv2.waitKey(1)&0xFF==ord("q"):
        break
    stream.seek(0)
    stream.truncate()
    cv2.destroyALLWindows()
