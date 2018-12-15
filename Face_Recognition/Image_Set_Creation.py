'''
Image_Set_Creation, Team Humanoid, IITK
    
    About:
        This code captures images from a camera, detects faces in it,
        and on recieving command, saves a cropped image of the face in 
        jpg format, having a name that is a code that we assign, and a 
        random number seperated by a '.' .
        
        It also creates a CSV file that stores the name and code of the
        person whose data set is being collected.
        These name and code are taken from the input.

    Known Bugs:
        Works poorly in low light.

        Can only detect faces in frontal orientation.

    Keys:
        SPACE : Capture Image.

        Q     : Exit.

    Destination of images and csv file have to be specified 
    to the code before running it.

'''

#import required libraries.
import cv2
import numpy as np 
import os
import random
import csv

#Load face detection cascade.
cascadePath = "Face_Sheet.xml"
faceCascade = cv2.CascadeClassifier(cascadePath)

#Initiate the camera.
cap=cv2.VideoCapture(0)

#set path for destination of the images clicked.
path='/home/deepank/Downloads/Face_Recognition/Image_Set'

#Input name and code number
print('Enter your name: ')
name=str(raw_input())
print('Enter your code: ')
code-int(raw_input())
name=name.upper()
#print('Running')

while True:

    #capture frames from camera and convert to grayscale.
    _,frame=cap.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    #find all the faces in the frame.
    faces=faceCascade.detectMultiScale(gray.copy(),1.3,5)
    #print('Face Detected')
    
    #draw rectangles on each face detected.
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
    
    #display processed image.
    cv2.imshow('Frame',frame)
    
    #wait for input from keyboard for a millisecond,
    k=cv2.waitKey(1) & 0xFF
    
    #if the input is a space, 
    if k==ord(' '):
        #print('Image Captured')
        
        #crop the region containing the face and resize it.
        # it is resized so that every image captured has he same dimentions.
        gray=gray[y:y+h,x:x+w]
        resized=cv2.resize(gray,(300,300),interpolation=cv2.INTER_AREA)
        
        #save the cropped image with the name format explained in the beginning.
        cv2.imwrite(os.path.join(path , str(code)+'.'+str(int(random.random()*1000000)))+'.jpg', resized)
    
    #if the input if 'q', 
    elif k==ord('q'):
        #create a row matrix to store name and code.
        row=[name,code]
        
        #open the csv file and add this row.
        with open('Data.csv','a') as f:
            write=csv.writer(f)
            write.writerow(row)
        break

#Release the camera and close all windows.
cap.release()
cv2.destroyAllWindows()


