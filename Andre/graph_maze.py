from graph_class import Graph
def graph_maze(maze):
    """
    Returns a dictionary representing the maze as a graph and a second dictionary containing the
    arc costs.

    Input:
    maze: 2d-list representing the maze as a grid. Free cells are maked as '0' and obstacles cells as '1'.

    Output:
    maze_dict: a dictionary representing the maze as a graph. For each key, maze_dict stores
    a list containing the 1st degree nodes as well as some relevant information.
    """
    n_row = len(maze)
    n_col = len(maze[0])
    actions = ((0,1,1),(-1,0,1),(0,-1,1),(1,0,1), (1,1,1.4),(1,-1,1.4),(-1,1,1.4),(-1,-1,1.4))
    graph = Graph()

    for row in range(n_row):
        for col in range(n_col):
            for action in actions:
                x = row + action[0]
                y = col + action[1]
                if 0 <= x and x < n_row and 0 <= y and y < n_col:
                    if maze[row][col] == 0: # if the cell is free
                        if maze[x][y] == 0: # if neighbor is free
                            graph.add_edge(action[2], (row, col), (x, y))
                        
                        





    return graph
