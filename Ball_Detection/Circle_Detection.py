
'''
Function: Detects largest circle lying in the given HSV range
Author: Madhur Deep Jain


Errors corrected:
    Old code registered cnt = cnts[0]
    -- had to remove this.

    While finding contours, old code used mask.
    -- changed it to mask.copy() so that original mask image is not altered.

    While finding contours we have to use three variable,
    old code used only which gave errors.

Known Bugs:
    -- The code depends on the color of the circle/ball.
    If the image frame has some region other than the ball having the same 
    color, and has a larger area, the code reports the center of that area.

    -- Cannot detect balls/circles of different colors together.

    -- Finds center of only one circle/ball.

    -- Have to calibrate manually using trackbars.

'''

import cv2
import numpy as np

#Empty function to be passed while creating trackbars.
def nothing(self):
    pass

#turn on the camera
cap = cv2.VideoCapture(0)

#####################################################################   
                                                                    #
# # HSV values for tennis ball                                      #   <-- use
# min_green = (30, 130, 60)                                         #   <-- these 
# max_green = (50, 255, 255)                                        #   <-- for
                                                                    #
# # HSV values for bull's eye                                       #   <-- calibration
# min_orange = (0, 120, 117)                                        #
# max_orange = (15, 250, 192)                                       #
                                                                    #
#####################################################################

#create a window for putting trackbars.
cv2.namedWindow('trackbars')

#create required variables.
hl='H_MIN'
hh='H_MAX'
sl='S_MIN'
sh='S_MAX'
vl='V_MIN'
vh='V_MAX'
rad='R_MIN'

#make trackbars.
cv2.createTrackbar(hl, 'trackbars', 30, 179, nothing)
cv2.createTrackbar(hh, 'trackbars', 50, 179, nothing)
cv2.createTrackbar(sl, 'trackbars', 130, 255, nothing)
cv2.createTrackbar(sh, 'trackbars', 255, 255, nothing)
cv2.createTrackbar(vl, 'trackbars', 60, 255, nothing)
cv2.createTrackbar(vh, 'trackbars', 255, 255, nothing)
cv2.createTrackbar(rad, 'trackbars', 5, 100, nothing)

while(True):

    #read image frames from the camera
    _, frame = cap.read()

    #get values from trackbars
    h_min = cv2.getTrackbarPos(hl, 'trackbars')
    h_max = cv2.getTrackbarPos(hh, 'trackbars')
    s_min = cv2.getTrackbarPos(sl, 'trackbars')
    s_max = cv2.getTrackbarPos(sh, 'trackbars')
    v_min = cv2.getTrackbarPos(vl, 'trackbars')
    v_max = cv2.getTrackbarPos(vh, 'trackbars')
    r_min = cv2.getTrackbarPos(rad, 'trackbars')

    #blur the image and convert color coding to HSV.
    kernal = np.ones((5,5), np.float32)/25
    blurred = cv2.filter2D(frame, -1, kernal)
    hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)

    #create arrays for storing minimum and maximum HSV values.
    HSV_MIN=np.array([h_min, s_min, v_min])
    HSV_MAX=np.array([h_max, s_max, v_max])

    #convert image to binary format.
    #keep region having desired colors in black turn rest to white.
    mask1 = cv2.inRange(hsv, HSV_MIN, HSV_MAX)
    
    #reduce noise.
    mask = cv2.erode(mask1, None, iterations=2)
    mask = cv2.dilate(mask, None, iterations=2)

    #find contours in the image.
    rel, cnts, hierarchy = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    center = None

    #check if cnts(containing contour arrays) is non empty.
    if len(cnts) > 0:
        
        #find the region with maximum area.
        cnt = max(cnts, key=cv2.contourArea)
        
        #get center and radius of the smallest circle enclosing the ball.
        ((x, y), radius) = cv2.minEnclosingCircle(cnt)
        
        #check if ball is large enough
        if radius > r_min:

            #find the center of the contour(ball).
            M = cv2.moments(cnt)
            center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
            print (center)

            #draw two circles: one showing boundary of the ball, other the center.
            cv2.circle(frame, (int(x), int(y)), int(radius), (0, 255, 255), 2)
            cv2.circle(frame, center, 5, (0, 0, 255), -1)

    #display relevent images.
    cv2.imshow('mask', mask)
    cv2.imshow('mask1',mask1)
    cv2.imshow('blurred',blurred)
    cv2.imshow('frame', frame)
    
    #ask the system to wait for user to press Q,
    #exit the loop on recieving the input.
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
#release the camera and close all windows.
cap.release()
cv2.destroyAllWindows()
