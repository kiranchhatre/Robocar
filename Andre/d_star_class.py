class D_Star:
    def __init__(self,graph):
        self.graph = graph
        self.open_list = []
        self.tag = {node:'New' for node in graph.vertices()}
        self.h = {}
        self.k = {}
        self.backpointer = {}

    def get_min_state(self):
        empty = (len(self.open_list) == 0)
        return self.open_list[0][1] if not empty else None
    def get_kmin(self):
        empty = (len(self.open_list) == 0)
        return self.open_list[0][0] if not empty else -1
    def remove_from_list(self):
        data = self.open_list.pop(0)
        self.tag[data[1]] = 'Closed'

    def process_state(self,info = False):
        position = self.get_min_state()
        if position == None:
            return -1
        k_old = self.get_kmin()
        self.remove_from_list()

        if k_old < self.h[position]:
            for neighbour in self.graph.get_neighbourhood(position):
                new_estimate = self.h[neighbour] + self.graph.get_cost(neighbour,position)
                if self.h[neighbour]<= k_old and self.h[position]>new_estimate:
                    self.backpointer[position] = neighbour
                    self.h[position] = new_estimate

        if k_old == self.h[position]:
            for neighbour in self.graph.get_neighbourhood(position):
                new_estimate = self.h[position] + self.graph.get_cost(position,neighbour)
                if self.tag[neighbour]=='New':
                    self.backpointer[neighbour] = position
                    self.insert(neighbour,new_estimate)
                elif (self.backpointer[neighbour]==position and self.h[neighbour]!= new_estimate):
                    self.backpointer[neighbour] = position
                    self.insert(neighbour,new_estimate)
                elif (self.backpointer[neighbour]!=position and self.h[neighbour]> new_estimate):
                    self.backpointer[neighbour] = position
                    self.insert(neighbour,new_estimate)



        else:
            for neighbour in self.graph.get_neighbourhood(position):
                new_estimate = self.h[position] + self.graph.get_cost(position,neighbour)
                if self.tag[neighbour] == 'New':
                    self.backpointer[neighbour] = position
                    self.insert(neighbour, new_estimate)
                elif (self.backpointer[neighbour]==position and self.h[neighbour]!= new_estimate):
                    self.backpointer[neighbour] = position
                    self.insert(neighbour, new_estimate)
                else:
                    if self.backpointer[neighbour]!=position and self.h[neighbour]>new_estimate:
                        self.insert(position,self.h[position])
                    else:
                        new_estimate = self.h[neighbour] + self.graph.get_cost(neighbour,position)
                        if self.backpointer[neighbour]!=position and self.h[position]> new_estimate and self.tag[neighbour]=='Closed' and self.h[neighbour]>k_old:
                            self.insert(neighbour,self.h[neighbour])
        if info:
            print('\nPosition')
            print(position)
            print('\nOpen list')
            print(self.open_list)
            print('\nkey value function')
            print(self.k[position])
            print('\ntags')
            print(self.tag[position])
            print('\nh value function')
            print(self.h[position])
            print('\nk_old: {}'.format(k_old))
            print('\nBackpointers')
            print(self.backpointer[position])
        return self.get_kmin()

    def modify_cost(self,X,Y,cval):
        self.graph.update_cost(cval,X,Y)
        if self.tag[X] == 'Closed':
            self.insert(X,self.h[X])
        return self.get_kmin()

    def insert(self,X,h_new):
        if self.tag[X]=='New':
            self.k[X] = h_new
            self.open_list.append([self.k[X],X])
            self.tag[X] = 'Open'
            self.open_list.sort()
        elif self.tag[X] == 'Open':
            if h_new < self.k[X]:
                self.open_list.remove([self.k[X],X])
                self.k[X] = h_new
                self.open_list.append([self.k[X],X])
                self.open_list.sort()
        else:
            self.k[X] = min(self.h[X],h_new)
            self.open_list.append([self.k[X],X])
            self.tag[X] = 'Open'
            self.open_list.sort()
        self.h[X] = h_new

    def perceive(self,position,new_cost):
        next_position = self.backpointer[position]
        expected = self.graph.get_cost(next_position,position)
        read = new_cost
        changed = not(expected == read)
        print(expected,' ', read, ' ', changed)
        return changed
