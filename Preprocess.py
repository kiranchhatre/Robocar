from cv2 import cv2
import numpy as np
from matplotlib import pyplot as plt
import pandas as pd


img_maze = cv2.imread('C:\\Users\\faube\\Desktop\\Python\\Data\\Maze_original.jpg')
rgb_image = cv2.cvtColor(img_maze, cv2.COLOR_BGR2RGB)

#Gray conversion
gray_image = cv2.cvtColor(rgb_image, cv2.COLOR_RGB2GRAY)

#Blur
#gray_image= cv2.GaussianBlur(gray_image,(21,21),0)

#Threshold
ret, threshold_image = cv2.threshold(gray_image,200, 255, 0)
#Resize
resized_image= cv2.resize(threshold_image, (0,0), fx=1, fy=1)
#Invert 
image_final = resized_image
image_final = cv2.bitwise_not(resized_image)

#Display
cv2.startWindowThread()

#SaveFile

cv2.imwrite('C:\\Users\\faube\\Desktop\\Python\\Data\\Maze_originalfinal.jpg',image_final)

#Detect Start and Finish

def findstart():
    global startpoint

    hsv_image = cv2.cvtColor(img_maze, cv2.COLOR_BGR2HSV)
  
   # define range of red color in HSV
    lower_red = np.array([160,100,100])
    upper_red = np.array([180,255,255])
   
    # Threshold the HSV image to get only blue colors
    mask = cv2.inRange(hsv_image, lower_red, upper_red)
    

    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(hsv_image,hsv_image, mask= mask)
    cimg=res
    res=cv2.cvtColor(res, cv2.COLOR_RGB2GRAY)


    circles = cv2.HoughCircles(res,cv2.HOUGH_GRADIENT,1,30,param1=50,param2=10,minRadius=0,maxRadius=0)
    #circles = np.uint16(np.around(circles))

    for i in circles[0,:]:
    # draw the outer circle
        cv2.circle(cimg,(i[0],i[1]),i[2],(255,0,0),2)
     # draw the center of the circle
        cv2.circle(cimg,(i[0],i[1]),2,(0,0,255),3)
        startpoint = (i[0],i[1])
    #print(startpoint)
    #cv2.imshow('Detected Start circles',cimg)
    #cv2.waitKey(0)

def findend():
    global endpoint

    hsv_image = cv2.cvtColor(img_maze, cv2.COLOR_BGR2HSV)
  
   # define range of red color in HSV
    lower_red = np.array([0,100,100])
    upper_red = np.array([135,255,255])
   
    # Threshold the HSV image to get only blue colors
    mask = cv2.inRange(hsv_image, lower_red, upper_red)
    

    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(hsv_image,hsv_image, mask= mask)
    cimg=res
    res=cv2.cvtColor(res, cv2.COLOR_RGB2GRAY)

    circles = cv2.HoughCircles(res,cv2.HOUGH_GRADIENT,1,30,param1=50,param2=10,minRadius=0,maxRadius=0)
    #circles = np.uint16(np.around(circles))

    for i in circles[0,:]:
    # draw the outer circle
        cv2.circle(cimg,(i[0],i[1]),i[2],(255,0,0),2)
     # draw the center of the circle
        cv2.circle(cimg,(i[0],i[1]),2,(0,0,255),3)
        endpoint = (i[0],i[1])
    #print(endpoint)
    #cv2.imshow('Detected End circles',cimg)
    #cv2.waitKey(0)

findstart()
findend()