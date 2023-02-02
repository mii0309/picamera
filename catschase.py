import cv2 
import sys 
import picamera.array
import picamera

cascade_file="cascade.xml"
with picamera.PiCamera() as camera:
  with picamera.array.PiRGBAarray(camera) as stream:
    camera.resolution=(320,240)
    while True:
      camera.capture(stream,'bgr',use_video_port=True)
      cascade=cv2.CascadeClassifier(cascadefilename)
#     if cascade.empty():
#        print('cannot load cascade file')
#       sys.exit(-1)
     objects=cascade.detectMultiScale(srcimg,1.1,3)
    
     for(x,y,w,h) in objects:
        print(x,y,w,h) 
        cv2.rectangle(stream.array, (x, y), (x+w, y+h), (0,0,255),5)
        cv2.imshow('frame',stream.array)
        
        if cv2.waitkey(1)&0xFF=ord("q"):
          break
          
        stream.seek(0)
        stream.truncate()
        cv2.destroyALLWindows()
