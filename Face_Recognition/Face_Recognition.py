'''
	Face_Recognition, Team Humanoid, IITK

	About:
		This code reads images, and a csv file to train itself for
		recognising people by looing at their faces(by a camera input).
		
		The CSV file contains names of certain people for which database 
		is available along with their code number.

	Known Bugs:
		Works poorly in low light.

		Can detect faces in frontal orientation only.

		Assigns any random code to the faces for which database is not 
		available.

		Depends on the other code (Image_Set_creation.py)

	Keys:
		Q      : Exit.
'''

#import required libraries.
import cv2, os
import numpy as np 
from PIL import Image
import csv

#Load face detection cascade.
face_cascade=cv2.CascadeClassifier('Face_Sheet.xml')

#Load inbuilt face recognition algorithm.
recognizer=cv2.face.LBPHFaceRecognizer_create()

#Specify paths where images are present.
path='/home/deepank/Downloads/Face_Recognition/Image_Set'
image_paths = [os.path.join(path, f) for f in os.listdir(path)]

#create empty matrices for storing images and labels.
images = []
labels = []

#Define function to read names and associated codes.
def find(code):
	
	#Open the file.
	with open('Data.csv', 'rt') as f:
		
		#read line by line, seperate strings within a line by ';'
		reader = csv.reader(f, delimiter=',')
		
		#return code number from each row.
		for row in reader:
			if str(code) == row[1]:
				return row[0]

#read image paths one by one,
for image_path in image_paths:
    
	#goto the image.
    image = Image.open(image_path)
    
    #create array for an image.
   	image_arr= np.array(image, 'uint8')
    
   	#find label of the image from image path(it has been seperated by a '.')
    l = int(os.path.split(image_path)[1].split(".")[0])
    
    #add this image to the 'images' matrix, and label to the 'labels' matrix.
    images.append(image_arr)
    labels.append(l)
    
    #show the image that have been loaded.
    cv2.imshow("Adding faces to traning set...", image_arr)
    cv2.waitKey(10)

#train the face detection algorithm with the images provided.
recognizer.train(images, np.array(labels))

#initialise the camera.
cap=cv2.VideoCapture(0)

while True:

	#Read frames from the camera and convert to grayscale.
	_,img=cap.read()
	gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

	#Detect all the faces in the frame.
	faces=face_cascade.detectMultiScale(gray.copy(),1.3,5)
	
	#for each face detected,
	for (x,y,w,h) in faces:
		
		#predict the identity of the person using the face rec algorithm we trained.
		predicted_code,conf=recognizer.predict(gray[y:y+h,x:x+h])
		
		#Draw rectangle surrounding the face detected.
		cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),3)
		
		#call the function 'find' defined earlier to find the name of the person from
		#data loaded from the CSV file and the code predicted by the algorithm.
		predicted_name=find(predicted_code)

		#print the  name of the person on the image under his face.
		cv2.putText(img,predicted_name,(x,y+h+20),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,255,0), 2)
		
		#display the processed image.
		cv2.imshow("Recognition",img)
	
	#wait for input from the user for a milisecond, exit on recieving input,
	#else repeat the process.
	if cv2.waitKey(1) & 0xFF==ord('q'):
		break

#release the camera and close all active windows.
cap.release()
cv2.destroyAllWindows()
