from tree_intersection import __version__
import pytest
from tree_intersection.tree_intersection import (
    binary_tree,
    tree_intersection,
    Node)

def test_version():
    assert __version__ == '0.1.0'


def test_tree_intersection(data) :
    assert tree_intersection(data[0],data[1]) == [100, 160, 125, 175, 200, 350, 500]

@pytest.fixture
def data() :
    tree_one = Node(150)
    tree_one.left = Node(100)
    tree_one.left.left = Node(75)
    tree_one.left.right = Node(160)
    tree_one.left.right.left = Node(125)
    tree_one.left.right.right = Node(175)
    tree_one.right = Node(250)
    tree_one.right.left = Node(200)
    tree_one.right.right = Node(350)
    tree_one.right.right.left = Node(300)
    tree_one.right.right.right = Node(500)
    binary_tree_one = binary_tree(tree_one)
    tree_two = Node(42)
    tree_two.left = Node(100)
    tree_two.left.left = Node(15)
    tree_two.left.right = Node(160)
    tree_two.left.right.left = Node(125)
    tree_two.left.right.right = Node(175)
    tree_two.right = Node(600)
    tree_two.right.left = Node(200)
    tree_two.right.right = Node(350)
    tree_two.right.right.left = Node(4)
    tree_two.right.right.right = Node(500)
    binary_tree_two = binary_tree(tree_two)

    return[binary_tree_one,binary_tree_two]
