from cv2 import cv2
import numpy as np
import threading
import colorsys
from Preprocess import startpoint,endpoint
class Point(object):

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


rw = 2
p = 0
start = Point()
end = Point()
SP = Point(int(startpoint[0]),int(startpoint[1]))
EP = Point(int(endpoint[0]),int(endpoint[1]))

dir4 = [Point(0, -1), Point(0, 1), Point(1, 0), Point(-1, 0)]


def BFS(s, e):

    global img, h, w, path, instruct
    const = 10000

    found = False
    q = []
    v = [[0 for j in range(w)] for i in range(h)]
    parent = [[Point() for j in range(w)] for i in range(h)]

    q.append(s)
    v[s.y][s.x] = 1
    while len(q) > 0:
        p = q.pop(0)
        for d in dir4:
            cell = p + d
            if (cell.x >= 0 and cell.x < w and cell.y >= 0 and cell.y < h and v[cell.y][cell.x] == 0 and
                    (img[cell.y][cell.x][0] != 0 or img[cell.y][cell.x][1] != 0 or img[cell.y][cell.x][2] != 0)):
                q.append(cell)
                v[cell.y][cell.x] = v[p.y][p.x] + 1  # Later

                img[cell.y][cell.x] = list(reversed(
                    [i * 255 for i in colorsys.hsv_to_rgb(v[cell.y][cell.x] / const, 1, 1)])
                )
                parent[cell.y][cell.x] = p
                if cell == e:
                    found = True
                    del q[:]
                    break

    path = []
    instruct = []

    if found:
        p = e
        while p != s:
            path.append(p)
            instruct.append(p)
            p = parent[p.y][p.x]
        path.append(p)
        path.reverse()

        for p in path:
            img[p.y][p.x] = [255, 255, 255]
            #print(p.x, '&', p.y)
        print("Path Found")
       
    else:
        print("Path Not Found")


def mouse_event(event, pX, pY, flags, param):

    global img, start, end, p

    if event == cv2.EVENT_LBUTTONUP:
        if p == 0:
            p += 2
    
def disp():
    global img
    cv2.imshow("Image", img)
    cv2.setMouseCallback('Image', mouse_event)
    while True:
        cv2.imshow("Image", img)
        cv2.waitKey(1)


img = cv2.imread("C:\\Users\\faube\\Desktop\\Python\\Data\\Maze_originalfinal.jpg", cv2.IMREAD_GRAYSCALE)
_, img = cv2.threshold(img, 120, 255, cv2.THRESH_BINARY)
img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
h, w = img.shape[:2]

print("Click to start calculation: ")

t = threading.Thread(target=disp, args=())
t.daemon = True
t.start()

while p < 2:
    pass

#BFS(start, end)
BFS(SP, EP)


#Create a text file with route
file = open("Route.txt","w")

for element in instruct:
    file.write(("{0},{1} \n".format(element.x, element.y)))
  
file.close()

cv2.waitKey(0)
