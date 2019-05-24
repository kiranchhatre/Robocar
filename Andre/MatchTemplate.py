from cv2 import cv2
import numpy as np
from matplotlib import pyplot as plt
import pandas as pd
import random
from Graph import Graph
#from MatchStart import startpoint,endpoint

img_maze = cv2.imread('C:\\Users\\faube\\Desktop\\Python\\Data\\demo.png',0)
img_maze_rgb = cv2.imread('C:\\Users\\faube\\Desktop\\Python\\Data\\demo.png')

def process_image(maze_raw):
    maze_raw_G = maze_raw[:,:,1]
    _, maze_raw_G = cv2.threshold(maze_raw_G,100,255,0)

    maze_raw_B = maze_raw[:,:,2]
    _, maze_raw_B = cv2.threshold(maze_raw_B,100,255,0)
    
    processed_image = maze_raw_B + maze_raw_G
    return processed_image

img_maze=process_image(img_maze_rgb)

template_cross=np.array([[255,255,255,0,0,0,255,255,255],
                         [255,255,255,0,0,0,255,255,255],
                         [255,255,255,0,0,0,255,255,255],
                         [0,0,0,0,0,0,0,0,0],
                         [0,0,0,0,0,0,0,0,0],
                         [0,0,0,0,0,0,0,0,0],
                         [255,255,255,0,0,0,255,255,255],
                         [255,255,255,0,0,0,255,255,255],
                         [255,255,255,0,0,0,255,255,255]],dtype=np.uint8)
template_corner_left=np.array([[255,255,255,255,255,255,255,255,255],
                                [255,255,255,255,255,255,255,255,255],
                                [255,255,255,255,255,255,255,255,255],
                                [0,0,0,0,0,0,255,255,255],
                                [0,0,0,0,0,0,255,255,255],
                                [0,0,0,0,0,0,255,255,255],
                                [255,255,255,0,0,0,255,255,255],
                                [255,255,255,0,0,0,255,255,255],
                                [255,255,255,0,0,0,255,255,255],],dtype=np.uint8)
template_corner_left_1=np.array([[255,255,255,0,0,0,255,255,255],
                                [255,255,255,0,0,0,255,255,255],
                                [255,255,255,0,0,0,255,255,255],
                                [0,0,0,0,0,0,255,255,255],
                                [0,0,0,0,0,0,255,255,255],
                                [0,0,0,0,0,0,255,255,255],
                                [255,255,255,255,255,255,255,255,255],
                                [255,255,255,255,255,255,255,255,255],
                                [255,255,255,255,255,255,255,255,255],],dtype=np.uint8)
template_corner_right_1=np.array([[255,255,255,0,0,0,255,255,255],
                                [255,255,255,0,0,0,255,255,255],
                                [255,255,255,0,0,0,255,255,255],
                                [255,255,255,0,0,0,0,0,0],
                                [255,255,255,0,0,0,0,0,0],
                                [255,255,255,0,0,0,0,0,0],
                                [255,255,255,255,255,255,255,255,255],
                                [255,255,255,255,255,255,255,255,255],
                                [255,255,255,255,255,255,255,255,255],],dtype=np.uint8)
template_corner_right=np.array([[255,255,255,255,255,255,255,255,255],
                                [255,255,255,255,255,255,255,255,255],
                                [255,255,255,255,255,255,255,255,255],
                                [255,255,255,0,0,0,0,0,0],
                                [255,255,255,0,0,0,0,0,0],
                                [255,255,255,0,0,0,0,0,0],
                                [255,255,255,0,0,0,255,255,255],
                                [255,255,255,0,0,0,255,255,255],
                                [255,255,255,0,0,0,255,255,255],],dtype=np.uint8)                                
template_t_right = np.array([[255,255,255,0,0,0,255,255,255],
                                [255,255,255,0,0,0,255,255,255],
                                [255,255,255,0,0,0,255,255,255],
                                [255,255,255,0,0,0,0,0,0],
                                [255,255,255,0,0,0,0,0,0],
                                [255,255,255,0,0,0,0,0,0],
                                [255,255,255,0,0,0,255,255,255],
                                [255,255,255,0,0,0,255,255,255],
                                [255,255,255,0,0,0,255,255,255],],dtype=np.uint8)    
template_t_left = np.array([[255,255,255,0,0,0,255,255,255],
                                [255,255,255,0,0,0,255,255,255],
                                [255,255,255,0,0,0,255,255,255],
                                [0,0,0,0,0,0,255,255,255],
                                [0,0,0,0,0,0,255,255,255],
                                [0,0,0,0,0,0,255,255,255],
                                [255,255,255,0,0,0,255,255,255],
                                [255,255,255,0,0,0,255,255,255],
                                [255,255,255,0,0,0,255,255,255],],dtype=np.uint8)    
template_t_bottom = np.array([[255,255,255,0,0,0,255,255,255],
                                [255,255,255,0,0,0,255,255,255],
                                [255,255,255,0,0,0,255,255,255],
                                [0,0,0,0,0,0,0,0,0],
                                [0,0,0,0,0,0,0,0,0],
                                [0,0,0,0,0,0,0,0,0],
                                [255,255,255,255,255,255,255,255,255],
                                [255,255,255,255,255,255,255,255,255],
                                [255,255,255,255,255,255,255,255,255],],dtype=np.uint8)   
template_t_top = np.array([[255,255,255,255,255,255,255,255,255],
                                [255,255,255,255,255,255,255,255,255],
                                [255,255,255,255,255,255,255,255,255],     [0,0,0,0,0,0,0,0,0],
                                [0,0,0,0,0,0,0,0,0],
                                [0,0,0,0,0,0,0,0,0],
                                [255,255,255,0,0,0,255,255,255],
                                [255,255,255,0,0,0,255,255,255],
                                [255,255,255,0,0,0,255,255,255]],dtype=np.uint8) 
template_end_left = np.array([[255,255,255,255,255,255,255,255,255],
                                [255,255,255,255,255,255,255,255,255],
                                [255,255,255,255,255,255,255,255,255],    
                                [0,0,0,0,0,0,255,255,255],
                                [0,0,0,0,0,0,255,255,255],
                                [0,0,0,0,0,0,255,255,255],
                                [255,255,255,255,255,255,255,255,255],
                                [255,255,255,255,255,255,255,255,255],
                                [255,255,255,255,255,255,255,255,255]],dtype=np.uint8)     
template_end_right = np.array([[255,255,255,255,255,255,255,255,255],
                                [255,255,255,255,255,255,255,255,255],
                                [255,255,255,255,255,255,255,255,255],    
                                [255,255,255,0,0,0,0,0,0],
                                [255,255,255,0,0,0,0,0,0],
                                [255,255,255,0,0,0,0,0,0],
                                [255,255,255,255,255,255,255,255,255],
                                [255,255,255,255,255,255,255,255,255],
                                [255,255,255,255,255,255,255,255,255]],dtype=np.uint8) 
template_end_bottom = np.array([[255,255,255,255,255,255,255,255,255],
                                [255,255,255,255,255,255,255,255,255],
                                [255,255,255,255,255,255,255,255,255],    
                                [255,255,255,0,0,0,255,255,255],
                                [255,255,255,0,0,0,255,255,255],
                                [255,255,255,0,0,0,255,255,255],
                                [255,255,255,0,0,0,255,255,255],
                                [255,255,255,0,0,0,255,255,255],
                                [255,255,255,0,0,0,255,255,255]],dtype=np.uint8) 
template_end_top = np.array([[255,255,255,0,0,0,255,255,255],
                                [255,255,255,0,0,0,255,255,255],
                                [255,255,255,0,0,0,255,255,255],    
                                [255,255,255,0,0,0,255,255,255],
                                [255,255,255,0,0,0,255,255,255],
                                [255,255,255,0,0,0,255,255,255],
                                [255,255,255,255,255,255,255,255,255],
                                [255,255,255,255,255,255,255,255,255],
                                [255,255,255,255,255,255,255,255,255]],dtype=np.uint8) 

intersections = [template_corner_left,template_corner_left_1,template_corner_right,template_corner_right_1,template_cross,template_t_bottom,template_t_left,template_t_right,template_t_top,template_end_bottom,template_end_left,template_end_right,template_end_top]
maze_copy=img_maze.copy()
Center_list_tmp=[]

for i in intersections:
    
    w, h = template_cross.shape[::-1]
    res = cv2.matchTemplate(img_maze,i,cv2.TM_CCOEFF_NORMED)
    threshold = 0.7
    loc = np.where( res >= threshold)
    for pt in zip(*loc[::-1]):
        #cv2.rectangle(img_maze_rgb, pt, (pt[0]+8, pt[1]+8), (0,0,255), 1)
        Center_list_tmp.append([pt[0]+5, pt[1]+5])
        # cv2.circle(img_maze_rgb,(pt[0]+4, pt[1]+4),1,(255,0,0), 1)
        #v.Circle(img, center, radius, color, thickness=1, lineType=8, shift=0) 
    cv2.imwrite('res.png',img_maze_rgb)
    cv2.imwrite('res1.png',img_maze)

  
#print(len(Center_list_tmp)) 
final_center_list = []

for x in Center_list_tmp:
    for y in Center_list_tmp[Center_list_tmp.index(x)+1:]:
        if abs(x[0]-y[0]) < 5 and abs(x[1]-y[1]) < 5:
            y[0] = 0
            y[1] = 0
        
           

center_list = list(filter(lambda k: k[0]!=0 and k[1] !=0, Center_list_tmp))

for element in center_list:
    cv2.circle(img_maze_rgb,tuple(element),1,(255,0,0), 1)
cv2.imwrite('res.png',img_maze_rgb)

center_list_flipped=[[t[1],t[0]] for t in center_list]  
            # print(type(x))
print(center_list) 
# print(len(new_list)) 
# print(maze_copy.shape)

def test_direction(picture, center_list,direction,position):

    shape = picture.shape

    neighbour = None
    cost = None


    x_center = position[0]
    y_center = position[1]

    if direction == 2: #go to the right
        x= x_center
        while x<shape[0]:
            x+=1
            if (picture[x,y_center,:]==255).all():
                break
            else:
                if [x,y_center] in center_list:
                    neighbour = [x,y_center]
                    cost = x
                    break


    if direction == -2: #go to the right
        x= x_center
        while x>=0:
            x-=1
            if (picture[x,y_center,:]==255).all():
                break
            else:
                if [x,y_center] in center_list:
                    neighbour = [x,y_center]
                    cost = x_center - x
                    break
    if direction == 1:
        y = y_center
        while y < shape[1]:
            y+=1
            if (picture[x_center,y,:] == 255).all():
                # print(picture[x_center,y,0])
                # print(picture[x_center,y,1])
                # print(picture[x_center,y,2])

                # print('test_1')
                break
            else:
                if [x_center,y] in center_list:
                    neighbour = [x_center, y]
                    cost = y
                    break
    if direction == -1:
        y = y_center
        while y >= 0:
            y-=1
            if (picture[x_center,y,:] == 255).all():
                break
            else:
                if [x_center,y] in center_list:
                    neighbour = [x_center, y]
                    cost = y_center - y
                    break

    return [cost, neighbour, direction]


def build_graph(picture, center_list):

    directions = [-1,1,-2,2]

    graph_dict = {}

    open_list = []
    closed_list = []

    position = random.choice(center_list)
    print('First position',position)

    open_list.append(position)

    while True:
        #print('Open List',open_list)
        for direction in directions:
            [cost, neighbour, action] = test_direction(picture,center_list,direction,position)
            if cost is not None:
                if tuple(position) in graph_dict.keys():
                    graph_dict[tuple(position)].append([cost, neighbour, action])
                else:
                    graph_dict[tuple(position)] = [[cost, neighbour, action]]
                
           

                
         
                if neighbour not in closed_list:
                    open_list.append(neighbour)
                print('Position',position)
                print('Open List',open_list)
        open_list.remove(position)
        closed_list.append(position)  
        if len(open_list)==0:
            break          
        position = random.choice(open_list)

    return graph_dict



graph_dict=build_graph(img_maze_rgb,center_list_flipped) 

print(len(graph_dict.keys()))