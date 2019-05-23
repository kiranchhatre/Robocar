

class DirectedGraph:
    """ A Python Class
    A simple Python graph class, demonstrating the essential
    facts and functionalities of graphs.
    """

    def __init__(self, graph_dict=None, cost = None):
        """ initializes a graph object
            If no dictionary or None is given,
            an empty dictionary will be used
        """
        if graph_dict == None:
            graph_dict = {}
        self.__graph_dict = graph_dict.copy()

        if cost == None:
            cost = {}
        self.__cost = cost.copy()

    def vertices(self):
        """ returns the vertices of a graph """
        return list(self.__graph_dict.keys())

    def edges(self):
        """ returns the edges of a graph """
        return self.__generate_edges()

    def add_vertex(self, vertex):
        """ If the vertex "vertex" is not in
            self.__graph_dict, a key "vertex" with an empty
            list as a value is added to the dictionary.
            Otherwise nothing has to be done.
        """
        if vertex not in self.__graph_dict:
            self.__graph_dict[vertex] = []

    def add_edge(self,cost,vertex1,vertex2):
        """ Adds an arc from "vertex2" to "vertex1" with cost "cost"
        """
        self.__cost[(vertex1,vertex2)] = cost


        if vertex2 in self.__graph_dict:
            self.__graph_dict[vertex2].append(vertex1)
        else:
            self.__graph_dict[vertex2] = [vertex1]
            
    
    
        


    def __generate_edges(self):
        """ A static method generating the edges of the
            graph "graph". Edges are represented as sets
            with one (a loop back to the vertex) or two
            vertices
        """
        edges = set()
        for vertex in self.__graph_dict:
            for neighbour in self.__graph_dict[vertex]:
                if (neighbour, vertex) not in edges:
                    edges.add((self.__cost[(neighbour,vertex)],neighbour, vertex))
        return edges

    def __str__(self):
        res = "vertices: "
        for k in self.__graph_dict:
            res += str(k) + " "
        res += "\nedges: "
        for edge in self.__generate_edges():
            res += str(edge) + " "
        return res

    def get_neighbourhood(self,vertex):
        """ Returns a list with the the arcs that connect the vertex to the neighbours"""
        return self.__graph_dict[vertex]
    def update_cost(self,new_cost,vertex1,vertex2):
        self.__cost[(vertex1,vertex2)] = new_cost
    def get_cost(self,vertex1,vertex2):
        return self.__cost[(vertex1,vertex2)]

class Graph:
    """ A Python Class
    A simple Python graph class, demonstrating the essential
    facts and functionalities of graphs.
    """

    def __init__(self, graph_dict=None, cost = None):
        """ initializes a graph object
            If no dictionary or None is given,
            an empty dictionary will be used
        """
        if graph_dict == None:
            graph_dict = {}
        self.__graph_dict = graph_dict.copy()

        if cost == None:
            cost = {}
        self.__cost = cost.copy()

    def vertices(self):
        """ returns the vertices of a graph """
        return list(self.__graph_dict.keys())

    def edges(self):
        """ returns the edges of a graph """
        return self.__generate_edges()

    def add_vertex(self, vertex):
        """ If the vertex "vertex" is not in
            self.__graph_dict, a key "vertex" with an empty
            list as a value is added to the dictionary.
            Otherwise nothing has to be done.
        """
        if vertex not in self.__graph_dict:
            self.__graph_dict[vertex] = set()

    def add_edge(self,cost,vertex1,vertex2):
        """ Adds an arc from "vertex2" to "vertex1" with cost "cost"
        """
        self.__cost[(vertex1,vertex2)] = cost
        self.__cost[(vertex2,vertex1)] = cost


        if vertex2 in self.__graph_dict:
            self.__graph_dict[vertex2].add(vertex1)
        else:
            self.__graph_dict[vertex2] = {vertex1}
        if vertex1 in self.__graph_dict:
            self.__graph_dict[vertex1].add(vertex2)
        else:
            self.__graph_dict[vertex1] = {vertex2}
            
    
    
        


    def __generate_edges(self):
        """ A static method generating the edges of the
            graph "graph". Edges are represented as sets
            with one (a loop back to the vertex) or two
            vertices
        """
        edges = []
        for vertex in self.__graph_dict:
            for neighbour in self.__graph_dict[vertex]:
                if {neighbour, vertex} not in edges:
                    edges.append({neighbour, vertex})
        return edges

    def __str__(self):
        res = "vertices: "
        for k in self.__graph_dict:
            res += str(k) + " "
        res += "\nedges: "
        for edge in self.__generate_edges():
            res += str(edge) + " "
        return res

    def get_neighbourhood(self,vertex):
        """ Returns a list with the the arcs that connect the vertex to the neighbours"""
        return self.__graph_dict[vertex]
    def update_cost(self,new_cost,vertex1,vertex2):
        self.__cost[(vertex1,vertex2)] = new_cost
        self.__cost[(vertex2,vertex1)] = new_cost

    def get_cost(self,vertex1,vertex2):
        return self.__cost[(vertex1,vertex2)]
    

