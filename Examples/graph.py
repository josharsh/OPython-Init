#Graph implementation using OOPS in Python
#Graph Class

'''A graph is a pictorial representation of a set of objects where some pairs of objects are connected by links. The interconnected objects are represented by points termed as vertices, and the links that connect the vertices are called edges.

Formally, a graph is a pair of sets (V, E), where V is the set of vertices and E is the set of edges, connecting the pairs of vertices.'''

class Graph(object):

    def __init__(self, graph_dict=None):
        """ initializes a graph object 
            If no dictionary or None is given, 
            an empty dictionary will be used
        """
        if graph_dict == None:
            graph_dict = {}
        self.__graph_dict = graph_dict

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

    def add_edge(self, edge):
        """ assumes that edge is of type set, tuple or list; 
            between two vertices can be multiple edges! 
        """
        edge = set(edge)
        (vertex1, vertex2) = tuple(edge)
        if vertex1 in self.__graph_dict:
            self.__graph_dict[vertex1].append(vertex2)
        else:
            self.__graph_dict[vertex1] = [vertex2]

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
                    edges.append({vertex, neighbour})
        return edges

    def __str__(self):
        """
        Return a string representation of the graph.

        Args:
            self: (todo): write your description
        """
        res = "vertices: "
        for k in self.__graph_dict:
            res += str(k) + " "
        res += "\nedges: "
        for edge in self.__generate_edges():
            res += str(edge) + " "
        return res


if __name__ == "__main__":

    g = { "a" : ["d"],
          "b" : ["c"],
          "c" : ["b", "c", "d", "e"],
          "d" : ["a", "c"],
          "e" : ["c"],
          "f" : []
        }

    '''Here, graph is a an object of class Grpah with the constructors passed with the parameter dictionary defined above as g
containing the vertices as key of dictionary and the values of key representing the adjacent neighbors. It will call the __str__ function with the dictionary
to form the respecting edges of the graph'''

    graph = Graph(g)

    #Printing the nodes of the graph
    print("Vertices of graph:")
    print(graph.vertices())
#Printing the edges of the graph
    print("Edges of graph:")
    print(graph.edges())
#Adding a new vertex to the above graph using  member function add_vertex
    print("Add vertex:")
    graph.add_vertex("z")
#Printing the new list of nodes
    print("Vertices of graph:")
    print(graph.vertices())
 #Adding a new edge to the graph from a node to z
    print("Add an edge:")
    graph.add_edge({"a","z"})
    
    print("Vertices of graph:")
    print(graph.vertices())
#Printing all the edges present in the graph
    print("Edges of graph:")
    print(graph.edges())

    print('Adding an edge {"x","y"} with new vertices:')
    graph.add_edge({"x","y"})
    print("Vertices of graph:")
    print(graph.vertices())
    print("Edges of graph:")
    print(graph.edges())
    
    ''' The corresponding output of the above:
    Vertices of graph:
    ['a', 'b', 'c', 'd', 'e', 'f']
    Edges of graph:
    [{'d', 'a'}, {'b', 'c'}, {'c'}, {'c', 'd'}, {'e', 'c'}]
    Add vertex:
    Vertices of graph:
    ['a', 'b', 'c', 'd', 'e', 'f', 'z']
    Add an edge:
    Vertices of graph:
    ['a', 'b', 'c', 'd', 'e', 'f', 'z']
    Edges of graph:
    [{'d', 'a'}, {'b', 'c'}, {'c'}, {'c', 'd'}, {'e', 'c'}, {'z', 'a'}]
    Adding an edge {"x","y"} with new vertices:
    Vertices of graph:
    ['a', 'b', 'c', 'd', 'e', 'f', 'z', 'y']
    Edges of graph:
    [{'d', 'a'}, {'b', 'c'}, {'c'}, {'c', 'd'}, {'e', 'c'}, {'z', 'a'}, {'y', 'x'}]'''

  