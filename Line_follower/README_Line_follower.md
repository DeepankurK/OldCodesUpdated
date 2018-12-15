# Read Me:- Line_follower.py  
 ## Table of Contents  
 - [Desciption](#discription)
- [Background](#background)   
- [Usage](#usage)
- [Short Comings](#short-comings)  
- [Maintainers](#maintainers)  
- [Contributors](#contributors)  
- [License](#license)  
 


## Description:
Read_me is written to facilitate the understanding of the code. 
 

The program finds the coordinates of the boundary of the segment of the line inside a narrow strip of image frame near the bot.


 


Using mathematical operations the position of line relative to the centerline of the image frame is found out and accordingly 'r', 'l' or 'f' which mean right, left and front respectively, are printed depicting the direction in which the bot should move to reach the line.


 


These characters are stored in the variable 'move' which can be passed to the ros for giving command to the bot to move in the desired direction.


 


Parameter t (line 102) has been calculated by taking ratio of the x coordinate of the bounding rectangle with the total width of the cropped image, and then subtracting it from 1, giving its relative position.


In the end multiply it by 5 to give some window for approximate comparison and account for whatever physical dimensions the line has.


 


if t is negative, line is on right side of center line, if positive, line is on left side, else in the center. we keep a range of 0.20 on either side to fit in the width of the line.

```sh
imx, imy, s = frame.shape
#get dimentions of the frame.
```
```sh
crop_img = frame[(2*imx)/3 : (3*imx)/4 , 0 : imy - 0]
#cropes the image.
#convertes cropped image to greyscale.
##IF BACKGROUND IS DARKER THAN LINE ADD THIS TO THE CODE.
#gray = cv2.bitwise_not(gray)
```


 


```sh
kernal = np.ones((5,5), np.float32)/25
mask = cv2.filter2D(gray, -1, kernal)
ret,thresh = cv2.threshold(mask,threshMin,255,cv2.THRESH_BINARY_INV)
#blur to remove noice and convert to binary image.
```




```sh
cnt = max(contours, key = cv2.contourArea)
#find contour with maximum area.
```


 


```sh
t = float(1.0 - 2.0*(cx /(imx - 20.0)))*5
#find relative position of bounding rectangle wrt center line in form of a parameter t.
```


 


```sh
move = ' '
if t > -0.20 and t < 0.20:
        move = 'f'
elif t <= -0.20:
        move = 'r'
elif t >= 0.20:
        move = 'l'
print(move, t)
#print ‘f’, ‘r’ or ‘l’ according to position.
```


 


```sh
cv2.drawContours(crop_img, [cnt], -1, (255,255,0), 3)
#draw contours of the line.
```




 
 
## Background  
Line_follower was first written in c++ under the summer project of Humanoid club, IIT kanpur.


It was written by Mrinal Dogra to work with a biped developed indigenously by the Club.


 


The code was updated by Madhur Deep Jain and Shashi Kant and is currently being moderated by Deepankur Kansal And Paras Mittal.


 
## Usage  
Click on the file Line_follower.py to get the full code.  
 
## Short Comings
1. Even if no line is present then also some direction is given as output
2. If two or more lines are given than then the code will not give correct output.
3. It will give a zig-zag pattern for slant path.


## Maintainers  
 
[@Deepankur Kansal]([https://github.com/DeepankurK](https://github.com/DeepankurK)).


[@Paras Mittal](https://github.com/Paras69/)  
 
## Contributors  
[@Shashi Kant](https://github.com/shashikg)
[@Madhur Deep Jain](https://github.com/madhurdeepjain)  
## License  
[IITK](LICENSE) © HUMANOID CLUB

