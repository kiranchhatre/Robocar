import cv2 as cv
import numpy as np
import random

def calculate_actions(maze_dict,current_position, pose, path):
    actions = []

    actions_matrice = np.array([[0,-2,0],[-1,0,1],[0,2,0]])
    for position in path:
        for i  in maze_dict[current_position]:
            print(i)
            if i[1]==position:
                action = i[2]
                assert action in [-1,1,-2,2]
        print(action)
        indexes = np.where(actions_matrice==action)
        print(indexes, type(indexes))
        indexes_np = np.array(indexes)
        print(pose, type(pose), pose.shape)
        indexes_np = indexes_np-1
        rot_matrix = get_rotation_matrix(pose)
        new_indexes = np.matmul(rot_matrix,indexes_np)
        new_indexes+=1
        print(new_indexes)
        new_action = actions_matrice[tuple(new_indexes.astype(int))]
        actions.append(new_action)
        print('new_action',new_action)
        pose = get_pose(action, pose)
        print('new_pose', pose)
        current_position  = position

    return actions


def get_pose(action, pose):
    assert action in [1,-1,2,-2], "Action non existent!"
    if action == 2:
        pose = np.array([[0],[-1]])
    elif action == 1:
        pose = np.array([[1],[0]])
    elif action == -1:
        pose = np.array([[-1],[0]])
    elif action == -2:
        pose = np.array([[0,1]])
    return pose
def get_rotation_matrix(pose):
    if (pose==np.array([[0],[1]])).all():
        rot_matrix = np.eye(2)
    elif (pose==np.array([[0],[-1]])).all():
        rot_matrix = -np.eye(2)
    elif (pose==np.array([[1],[0]])).all():
        rot_matrix = np.array([[0,-1],[1,0]])
    elif (pose==np.array([[-1],[0]])).all():
        rot_matrix = -np.array([[0,-1],[1,0]])
    return rot_matrix

def djikstra(maze_dict,start,goal, verbose = False):


    #maze_dict = graph_maze(maze)

    #start_position = (start[0],start[1])
    #goal_position = (goal[0],goal[1])


    open_list = []
    closed_list = []
    backpointer = {}
    path = []
    found = False
    resign = False

    x = start
    g = 0

    open_list.append((g,x))
    closed_list.append(x)
    steps = 0


    while not resign and not found:
        if verbose:
            print('Step {}'.format(steps))
            print('Open list:')
            print(open_list)
            print('Closed list')
            print(closed_list,end = '\n\n')
        if len(open_list)==0:
            print('It is impossible to solve this maze.')
            resign = True
        else:
            open_list.sort()
            current = open_list.pop(0)
            x = current[1]
            g = current[0]
            if x==goal:
                print('Goal reached in {} steps'.format(steps))
                found = True
                move_steps = 0
                path.append(x)
                while (x != start):
                    x = backpointer[x]
                    move_steps+=1
                    path.append(x)
                path.reverse()
                for node in path:
                    print('Node: {}'.format(node))
                print('Total cost: {}'.format(g))

            else:
                for neighbour in maze_dict[x]:
                    if neighbour[1] not in closed_list:
                        x2 = neighbour[1]
                        g2 = neighbour[0] + g
                        backpointer[x2] = x
                        open_list.append((g2,x2))
                        closed_list.append(x2)
        steps+=1
    print('Total time steps: {}'.format(steps))
    return path


def get_graph(text):
    f = open(text)
    info = []
    while True:
        line = f.readline()
        if line == '':
            break
        else:
            info.append(line)
    f.close()

    total_nodes = int(info[0].split('-')[1])
    start_node = int(info[1].split('-')[1])
    end_node = int(info[2].split('-')[1])

    graph_info = info[3:]

    graph_dict = {}
    for line in graph_info:
        l = line.split(',')
        nodes = l[0].split('-')
        node_1 = int(nodes[0])
        node_2 = int(nodes[1])
        distance = int(l[1])
        action = int(l[2])
        if node_1 in graph_dict.keys():
            graph_dict[node_1].append([distance, node_2,action])
        else:
            graph_dict[node_1] = []
            graph_dict[node_1].append([distance, node_2,action])
        if node_2 in graph_dict.keys():
            graph_dict[node_2].append([distance, node_1, -action])
        else:
            graph_dict[node_2] = []
            graph_dict[node_2].append([distance, node_1, -action])
    assert total_nodes == len(graph_dict.keys()), 'Fuck! Something is wrong'
    return start_node, end_node, graph_dict

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
                print(picture[x_center,y,0])
                print(picture[x_center,y,1])
                print(picture[x_center,y,2])

                print('test_1')
                break
            else:
                print('test_2')
                if [x_center,y] in center_list:
                    print('test_3')
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

    open_list.append(position)

    while True:
        for direction in directions:
            [cost, neighbour, action] = test_direction(picture,center_list,direction,position)
            if cost is not None:
                if tuple(position) in graph_dict.keys():
                    graph_dict[tuple(position)].append([cost, neighbour, action])
                else:
                    graph_dict[tuple(position)] = [[cost, neighbour, action]]

                if neighbour not in closed_list:
                    open_list.append(neighbour)
        open_list.remove(position)
        closed_list.append(position)
        if len(open_list)==0:
            break
        position = random.choice(open_list)

    return graph_dict

def process_image(maze_raw):
    maze_raw_G = maze_raw[:,:,1]
    _, maze_raw_G = cv.threshold(maze_raw_G,100,255,0)

    maze_raw_B = maze_raw[:,:,2]
    _, maze_raw_B = cv.threshold(maze_raw_B,100,255,0)
    
    processed_image = maze_raw_B + maze_raw_G
    return processed_image
