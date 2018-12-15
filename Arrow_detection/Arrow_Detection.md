# Read Me:- Face_Recgnition.py
 
  

## Table of Contents

  
- [Description](#dscription)

  

- [Background](#background) 
- [Usage](#sage)
- [Short Comings](#shortcomings)  
- [Contributors](#contributors)
- [Maintainers](#maintainers)
- [License](#license) 


 ## Description
 Read_me is written to facilitate the understanding of the code.
This code detects arrows and determine the direction they
are pointing in. 
```sh
cv2.namedWindow("control")
cv2.createTrackbar("thresh_min", "control", 60, 255, nothing)
#create trackbar to control min thresh values.
```
```sh
ret, thresh = cv2.threshold(mask, thresh_min, 255, cv2.THRESH_BINARY_INV)
#Convert image to binary color code.	 
 #IF BACKGROUND IS DARKER THAN ARROW, ADD THIS TO THE CODE
#thresh = cv2.bitwise_not(thresh)
```
```sh
x, y, w, h = cv2.boundingRect(cnt)
#find coordinates of the min bounding rectangle of that contour.
```
```sh
roi = thresh[y + (7*h/9) : y + (8*h/9), x : x + w]
#crop image to extract that bounding rectangle.
```
```sh
#draw the boundary of roi on the original image.
cv2.rectangle(frame, (x, y + (7*h/9)), (x + w, y + (8*h/9)), (255, 0, 0) 2)
```
```sh
ret, contours2, hierarchy2 = cv2.findContours(roi, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE
#find contours inside roi
```
```sh
cnt2 = max(contours2, key = cv2.contourArea)
# find the one with largest area.
```
```sh
t = float(1.0 - 2.0*(cx /(r_wid)))*5
'''
	t here is a parameter that stores the relative position 
	of the base of the arrow wrt the center line of the roi.

	it is calculated by taking ratio of the x coordinate to
	the half of the total width of the roi and substracting 
	it from 1. multiply it by 5 to reduce degree of approximation.
	If t is negative, it means base line is to the left of center,
	else to the right.
'''
```
```sh
#if base line is on the left, the arrow head is on the right
#and vice versa. If it is in the middle, this is a straight arrow.
#check the conditions and assign 'f', 'r' or 'l' accordingly.
	if t > -10.0 and t < 10.0:
		move = 'f'
	elif t <= -10.0:
		move = 'r'
	elif t >= 10.0:
		move = 'l'
```
## Background  
Arrow_Detection.py was created in the summer term by the Humanoid team, IITK .
It is a step towards the dream of Humanoid team to develop a fully functional self indigenous humanoid.
It was created by Himanshu, Madhur Deep Jain,Amar and Ankush.
Keys:  Q     : Exit.

## Usage  
Click on the file Arrow_Detection.py to get the full code.
Keys:     Q     : Exit.
## Short Comings
Depends highly on the orientation of the camera.
Works only for certain types of arrows:		
```sh
 #####>         ^           <####
 #	        #               #  
 #	        #               #
 #              #               #
 ```
## Maintainers  
[@Deepankur Kansal](https://github.com/DeepankurK)

[@Paras Mittal](https://github.com/Paras69/)

## Contributors
[@Himanshu Verma](https://github.com/himanshu11235)
[@Madhur Deep Jain](https://github.com/madhurdeepjain?fbclid=IwAR3c1uZx80FQGu-BakDqOjhv8uaLuzYapbOyFGdw9eB8YyjvEVmleAXwnqo)
## License
[IITK](LICENSE) © HUMANOID CLUBTEAM

