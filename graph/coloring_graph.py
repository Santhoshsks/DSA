class Graph:
    def __init__(self, num_of_vertex, directed=False):
        self.m_num_of_vertex = num_of_vertex
        self.m_vertex = range(self.m_num_of_vertex)
        self.m_directed = directed
        self.m_adj_list = {vertex: [] for vertex in self.m_vertex}

    def add_edge(self, vertex1, vertex2):
        self.m_adj_list[vertex1].append(vertex2)
        if not self.m_directed:
            self.m_adj_list[vertex2].append(vertex1)

    def print_adj_list(self):
        for key in self.m_adj_list.keys():
            print("vertex", key, ": ", self.m_adj_list[key])

    def graph_coloring(self):
        solution={}
        answer=True
        for i in self.m_adj_list.keys():
            if i not in solution:
                solution[i]="Red"
                for j in self.m_adj_list[i]:
                        if j not in solution:
                            solution[j]="Green"                
            if i in solution:
                if solution[i]=="Red":
                    for j in self.m_adj_list[i]:
                            if j not in solution:
                                solution[j]="Green"
                            else:
                                if solution[i]==solution[j]:
                                    answer=False
                                    break
                elif solution[i]=="Green":
                    for j in self.m_adj_list[i]:
                            if j not in solution:
                                solution[j]="Red"
                            else:
                                if solution[i]==solution[j]:
                                    answer=False
                                    break
    
        if answer:
            print("Solution Present")
            print("Solution:",solution)
        else:
            print("Solution Not Present")
graph = Graph(5)

graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(1, 3)
graph.add_edge(3, 4)
graph.add_edge(3, 4)

graph.print_adj_list()#printing graph

graph.graph_coloring()#coloring function
