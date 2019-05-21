from cv2 import cv2
import numpy as np
from matplotlib import pyplot as plt
import pandas as pd


img_maze = cv2.imread('C:\\Users\\faube\\Desktop\\Python\\Data\\maze.jpg')
rgb_image = cv2.cvtColor(img_maze, cv2.COLOR_BGR2RGB)

#Gray conversion
gray_image = cv2.cvtColor(img_maze, cv2.COLOR_RGB2GRAY)

#Blur
gray_image= cv2.GaussianBlur(gray_image,(21,21),0)

#Threshold
ret, threshold_image = cv2.threshold(gray_image,110, 255, 0)
#Resize
resized_image= cv2.resize(threshold_image, (0,0), fx=0.2, fy=0.2)
#Invert 
image_final = resized_image
#image_final = cv2.bitwise_not(resized_image)

#Display
cv2.startWindowThread()
#cv2.namedWindow("Image")
cv2.imshow('Image',image_final)
cv2.waitKey(0)

#SaveFile

cv2.imwrite('C:\\Users\\faube\\Desktop\\Python\\Data\\Maze_1final.jpg',image_final)

#Detect Start and Finish

def startpoint():
    resized_image_start= cv2.resize(img_maze, (0,0), fx=0.2, fy=0.2)
    hsv_image = cv2.cvtColor(resized_image_start, cv2.COLOR_BGR2HSV)
  
   # define range of red color in HSV
    lower_red = np.array([0,100,100])
    upper_red = np.array([10,255,255])

    # Threshold the HSV image to get only blue colors
    mask = cv2.inRange(hsv_image, lower_red, upper_red)

    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(hsv_image,hsv_image, mask= mask)
    cimg=res
    res=cv2.cvtColor(res, cv2.COLOR_RGB2GRAY)
    cv2.imshow('Start',res)
    cv2.waitKey(0)

    circles = cv2.HoughCircles(res,cv2.HOUGH_GRADIENT,1,20, param1=50,param2=30,minRadius=0,maxRadius=0)
    circles = np.uint16(np.around(circles))

    for i in circles[0,:]:
    # draw the outer circle
        cv2.circle(cimg,(i[0],i[1]),i[2],(255,0,0),2)
     # draw the center of the circle
        cv2.circle(cimg,(i[0],i[1]),2,(0,0,255),3)
    
    cv2.imshow('detected circles',cimg)
    cv2.waitKey(0)

startpoint()