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
#    assert graph.get_nodes() == dict_keys(['A', 'B', 'C', 'D', 'E'])
#    assert graph.get_neighbors(v1) == [('B', 1), ('C', 2)]
#    assert graph.get_neighbors(v2) == [('D', 4)]
#    assert graph.get_neighbors(v3) == [('D', 8), ('E', 3)]
#    assert graph.get_neighbors(v4) == [('E', 5)]
#    assert graph.get_neighbors() == {'A': [('B', 1), ('C', 2)], 'B': [('D', 4)], 'C': [('D', 8), ('E', 3)], 'D': [('E', 5)], 'E': []}
