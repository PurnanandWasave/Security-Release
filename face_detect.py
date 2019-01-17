import cv2
import numpy as np

# Haar Cascade 
face_cascade = cv2.CascadeClassifier('haar_cascade_files/haarcascade_frontalface_default.xml')

if face_cascade.empty():
  raise IOError('Unable to load face cascade classifier xml file')

# Video capturing and scaling
cap = cv2.VideoCapture(0)

scaling_factor = 0.5


#Capture frame
while True:
  _, frame = cap.read()
  
  
#Resize frame 
  frame = cv2.resize(frame, None, fx=scaling_factor, fy=scaling_factor, interpolation=cv2.INTER_AREA)


#Image to grayscale conversion
  gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

#Running face detecor on gray image
  face_rects = face_cascde.detectMultiScale(gray, 1.3, 5)

#Detected face
  for(x,y,w,h) in face_rects:
    cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 3)
  
#output
  cv2.imshow('face detector', frame)

#exit the loop
  c = cv2.waitKey(1)
  if c == 27:
    break
  
  
#Release the video capture
cap.release()
cv2.destroyAllWindows()


## Face Detector is ready ##



  

  
  
  

