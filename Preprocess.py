from cv2 import cv2
import numpy as np
from matplotlib import pyplot as plt
import pandas as pd


img_maze = cv2.imread('C:\\Users\\faube\\Desktop\\Python\\Data\\maze_1.jpg')
rgb_image = cv2.cvtColor(img_maze, cv2.COLOR_BGR2RGB)

#Gray conversion
gray_image = cv2.cvtColor(img_maze, cv2.COLOR_RGB2GRAY)

#Blur
gray_image= cv2.GaussianBlur(gray_image,(21,21),0)

#Threshold
ret, threshold_image = cv2.threshold(gray_image,110, 255, 0)
#Resize
resized_image= cv2.resize(threshold_image, (0,0), fx=0.5, fy=0.5)
#Invert 
image_final = resized_image
#image_final = cv2.bitwise_not(resized_image)

#Display
cv2.startWindowThread()
#cv2.namedWindow("Image")
cv2.imshow('Image',image_final)
cv2.waitKey(5)

#SaveFile

cv2.imwrite('C:\\Users\\faube\\Desktop\\Python\\Data\\Maze_1final.jpg',image_final)

