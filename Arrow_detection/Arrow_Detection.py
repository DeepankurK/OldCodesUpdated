'''
	About:
		This code detects arrows and determine the direction they
		are pointing in. 

	Known Bugs:
		Depends highly on the orientation of the camera.

		Works only for certain types of arrows:
		
		#####>     ^      <####
 		#	   #	      #    --> only bent arrows and forward arrow.
		#	   #	      #
		#	   #          #
'''

#import required libraries.
import cv2
import numpy as np 

#create an empty fuction to bw passes while creating trackbars.
def nothing():
	pass
#create trackbar to control min thresh values.
cv2.namedWindow("control")
cv2.createTrackbar("thresh_min", "control", 60, 255, nothing)

#Initiate camera capture.
cam = cv2.VideoCapture(0)

while True:
	
	#Read images from camera, and convert to grayscale.
	rel, frame = cam.read()
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

	#recieve input from trackbar.
	thresh_min = cv2.getTrackbarPos('thresh_min', 'control')
	
	#blur the image.
	kernal = np.ones((5,5), np.float32)/25
	mask = cv2.filter2D(gray.copy(), -1, kernal)
	
	#Convert image to binary color code.
	ret, thresh = cv2.threshold(mask, thresh_min, 255, cv2.THRESH_BINARY_INV)

	#IF BACKGROUND IS DARKER THAN ARROW, ADD THIS TO THE CODE
	#thresh = cv2.bitwise_not(thresh)

	#find all the contours in the image.
	ret, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

	#Check if contours is empty, if not, find the one with max area.
	if len(contours) > 0:	
		cnt = max(contours, key = cv2.contourArea)

		#find coordinates of the min bounding rectangle of that contour.
		x, y, w, h = cv2.boundingRect(cnt)
		
		#crop image to extract that bounding rectangle.
		roi = thresh[y + (7*h/9) : y + (8*h/9), x : x + w]

		#draw the boundary of roi on the original image.
		cv2.rectangle(frame, (x, y + (7*h/9)), (x + w, y + (8*h/9)), (255, 0, 0) 2)

		#display roi.
		cv2.imshow('roi', roi)

		#find contours inside roi.
		ret, contours2, hierarchy2 = cv2.findContours(roi, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)	
		
		#check if contours2 is empty, if not find the one with largest area.
		if len(contours2) > 0:
			cnt2 = max(contours2, key = cv2.contourArea)
			
			#find coordinates of the min bounding rectangle of that contour.
			rx, ry, rw, rh = cv2.boundingRect(cnt2)
			
			#find x coordinate of the middle of that rectangle.
			cx = float(rx - (rw/2))
			
			#find dimentions of roi image.
			r_wid, r_hi = roi.shape
			
			'''
				t here is a parameter that stores the relative position 
				of the base of the arrow wrt the center line of the roi.

				it is calculated by taking ratio of the x coordinate to
				the half of the total width of the roi and substracting 
				it from 1. multiply it by 5 to reduce degree of approximation.
				If t is negative, it means base line is to the left of center,
				else to the right.

			'''
			t = float(1.0 - 2.0*(cx /(r_wid)))*5

			move = ''

			#if base line is on the left, the arrow head is on the right
			#and vice versa. If it is in the middle, this is a straight arrow.
			#check the conditions and assign 'f', 'r' or 'l' accordingly.
			if t > -10.0 and t < 10.0:
				move = 'f'
			elif t <= -10.0:
				move = 'r'
			elif t >= 10.0:
				move = 'l'

			#print the instruction, and t(for calliberation)
			print(move, t)

	#Draw bounding rectangle of the largest contour.
	cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
	
	#Display images.
	cv2.imshow('frame', frame)
	cv2.imshow('thresh', thresh)
	
	#wait for user to input 'q', if recieved, exit loop.
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
#release the camera and close the windows.
cam.release()
cv2.destroyAllWindows()


