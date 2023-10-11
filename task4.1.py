'''
References:
https://docs.opencv.org/4.x/df/d9d/tutorial_py_colorspaces.html
https://docs.opencv.org/4.x/dd/d49/tutorial_py_contour_features.html
Improvements: Turn res from BGR to GRAY. 
              Add a if statement for contours so the program doesn't end if it did not capture the object.
'''
import numpy as np
import cv2 as cv


cap = cv.VideoCapture(0)
while(1):
    # Take each frame
    _, frame = cap.read()
    # Convert BGR to HSV
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    # define range of blue color in HSV
    lower_blue = np.array([110,50,50])
    upper_blue = np.array([130,255,255])
    # Threshold the HSV image to get only blue colors
    mask = cv.inRange(hsv, lower_blue, upper_blue)
    # Bitwise-AND mask and original image
    res = cv.bitwise_and(frame,frame, mask= mask)

    gray = cv.cvtColor(res, cv.COLOR_BGR2GRAY)
    ret,thresh = cv.threshold(gray,127,255,0)
    contours,hierarchy = cv.findContours(thresh, 1, 2)
    
    if contours:
        cnt = contours[0]
    # M = cv.moments(cnt)
    # print( M )
        x,y,w,h = cv.boundingRect(cnt)
        cv.rectangle(res,(x,y),(x+w,y+h),(0,255,0),2)

    #cv.imshow('frame',frame)
    #cv.imshow('mask',mask)
    cv.imshow('res',res)
    
    k = cv.waitKey(5) & 0xFF
    if k == 27:
        break

cv.destroyAllWindows()
