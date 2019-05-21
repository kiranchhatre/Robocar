from cv2 import cv2
import numpy as np
from matplotlib import pyplot as plt
import pandas as pd

#Import as Array
route = np.loadtxt('C:\\Users\\faube\\Desktop\\Python\\Robocar\\Route.txt',dtype=int, delimiter=',')
img = cv2.imread("C:\\Users\\faube\\Desktop\\Python\\Data\\Maze_originalfinal.jpg", cv2.IMREAD_GRAYSCALE)

class Point(object):

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

currentx = 280
currenty = 200


Pose = Point(currentx,currenty)

img = cv2.rectangle(img, (currentx-10 ,currenty),(currentx + 10, currenty), (0, 0, 0), 5)
cv2.imshow('Neuer Pfad',img)
cv2.waitKey(0)