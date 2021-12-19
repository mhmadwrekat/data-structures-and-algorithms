from graph import __version__
import pytest
from graph.graph import Graph

def test_version():
    assert __version__ == '0.1.0'

def test_graph() :
    graph = Graph()
    v1 = graph.add_node('A')
    v2 = graph.add_node('B')
    v3 = graph.add_node('C')
    v4 = graph.add_node('D')
    v5 = graph.add_node('E')
    graph.add_edge(v1, v2, 1)
    graph.add_edge(v1, v3, 2)
    graph.add_edge(v2, v4, 4)
    graph.add_edge(v3, v4, 8)
    graph.add_edge(v3, v5, 3)
    graph.add_edge(v4, v5, 5)
    assert graph.size() == 5
    assert graph.get_neighbors(v5) == []

################### Challenge 36 ########################
################ graph_breadth_first ####################
def test_breath_first_search() :
    graph = Graph()
    v1 = graph.add_node('A')
    v2 = graph.add_node('B')
    v3 = graph.add_node('C')
    v4 = graph.add_node('D')
    v5 = graph.add_node('E')
    graph.add_edge(v1,v2,1)
    graph.add_edge(v1,v3,2)
    graph.add_edge(v2,v4,4)
    graph.add_edge(v3,v4,8)
    graph.add_edge(v3,v5,3)
    graph.add_edge(v4,v5,5)
    graph.add_edge(v2,v1,10)
#    assert graph.graph_breadth_first(v1) == ['A', 'B', 'C', 'D', 'E']
#    assert graph.graph_breadth_first(v2) == ['B', 'D', 'A', 'E', 'C']
#    assert graph.graph_breadth_first(v3) == ['C', 'D', 'E', 'A', 'B']
#    assert graph.graph_breadth_first(v4) == ['D', 'E', 'C', 'A', 'B']
#    assert graph.graph_breadth_first(v5) == ['E', 'C', 'D', 'A', 'B']
