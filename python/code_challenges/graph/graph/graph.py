from collections import deque

class Vertex :
    """
    Input : value
    What is doing : Store The value
    Return : None
    """
    def __init__(self, value) :
        self.value = value
    def __str__(self) :
        return f'{self.value}'

class Queue :
    def __init__(self) :
        self.dq = deque()
    def enqueue(self, value) :
        self.dq.append(value)
    def dequeue(self) :
        return self.dq.pop(0)
    def __len__(self) :
        return len(self.dq)

class Edge :
    """
    Input : vertex, weight
    What is doing : store the vertex and the weight
    Return : None
    """
    def __init__(self, vertex, weight) :
        self.vertex = vertex
        self.weight = weight
    def __str__(self) :
        return f'{self.vertex} | {self.weight}'

class Graph :
    """
    Input : None
    What is doing : It is Creating an empty graph
    Return : None
    """
    def __init__(self) :
        self.__adj_list = {}
    """
    Input : value
    What is doing : add node to the graph
    Return : node
    """
    def add_node(self, value) :
        node = Vertex(value)
        self.__adj_list[node] = []
        return node
    """
    Input : start_vertex, end_vertex, weight
    What is doing : create an edge and append the edge to the value of start_vertex inside the adj_list
    Return : None
    """
    def add_edge(self, start_vertex, end_vertex, weight = 0) :
        if start_vertex not in self.__adj_list :
            raise KeyError('Start Vertex is not found in the Graph')
        if end_vertex not in self.__adj_list :
            raise KeyError('End Vertex is not found in the Graph')
        edge = Edge(end_vertex, weight)
        self.__adj_list[start_vertex].append(edge)
    """
    Input : vertex
    What is doing : Get all neighbors for a vertex
    Return : a list of edges
    """
    def get_neighbors(self, vertex) :
        return self.__adj_list.get(vertex, [])
    """
    Input : None
    What is doing : Get all The nodes in the graph as a set or list
    Return : a list or set of the nodes
    """
    def get_nodes(self) :
        return self.__adj_list.keys()
    """
    Input : None
    What is doing : find the length of the adj_list
    Return : int The size(the length of adj_list)
    """
    def size(self) :
        return len(self.__adj_list)

################### Challenge 36 ########################
################ graph_breadth_first ####################
    """
    Input : start_vertex
    What is doing : it will traverse throught all nodes
    Return : A list of nodes
    """
    def graph_breadth_first(self, start_vertex) :
        queue = Queue()
        result = []
        visited = set()
        queue.enqueue(start_vertex)
        visited.add(start_vertex)
        while len(queue) :
            current_vertex = queue.dequeue()
            neighbors = self.get_neighbors(current_vertex)
            for edge in neighbors :
                neighbors = edge.vertex
                if neighbors not in visited :
                    queue.enqueue(neighbors)
                    visited.add(neighbors)
                    result.append(neighbors)
        return result

################### Challenge 37 ########################
################# graph-business-trip ###################
    def business_trip(self,cities:list) :
        sum = 0
        flag = False
        for i in range(len(cities)-1) :
            neighbors = self.__adj_list[cities[i]]
            print(neighbors)
            for neighbor in neighbors :
                if cities[i + 1] == neighbor[0] :
                    sum += neighbor[1]
                    flag = True
                    break
                else :
                    sum += 0
                    flag = False
        if not flag :
            return False,'$0'
        return True,'$'+ str(sum)

################### Challenge 38 ########################
################### graph_depth_first ###################
    def graph_depth_first(self, node) :
        visited = set()
        visited.add(node)
        depth_first_list = []
        def __DFS(node, visited, depth_first_list) :
            visited.add(node)
            depth_first_list.append(node.value)
            neighbors = self.get_neighbors(node)
            if neighbors != 'Empty' :
                for i in neighbors :
                    if i.vertex not in visited :
                        __DFS(i.vertex, visited, depth_first_list)
        __DFS(node,visited,depth_first_list)
        return depth_first_list

print(Vertex(5))
print(Edge(4,8))
