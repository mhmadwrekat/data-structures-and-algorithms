
from trees import __version__
from trees.Trees import BinaryTree, Node
import pytest
def test_version():
    assert __version__ == '0.1.0'
# Test.1
def test_empty_tree() :
    tree = BinaryTree()
    assert tree.root == None
# Test.2
def test_single_root() :
    tree = BinaryTree()
    tree.root = Node("Wrekat")
    assert tree.root.value == "Wrekat"
# Test.3
def test_left_child(data) :
    assert data.root.left.value == "B"
# Test.4
def test_right_child(data) :
    assert data.root.right.value == "C"
# Test.5
def test_pre_order(data) :
    traveres = data.pre_order()
    expected = ["A","B","D","E","C","F"]
    assert traveres(data.root) == expected
# Test.6
def test_in_order(data) :
    traveres = data.in_order()
    expected = ["D","B","E","A","F","C"]
    assert traveres(data.root) == expected
# Test.7
def test_post_order(data) :
    traveres = data.post_order()
    expected = ["D","E","B","F","C","A"]
    assert traveres(data.root) == expected
# Tree Data
@pytest.fixture
def data () :
    tree = BinaryTree()
    tree.root = Node("A")
    tree.root.left = Node("B")
    tree.root.right = Node("C")
    tree.root.left.left = Node("D")
    tree.root.left.right = Node("E")
    tree.root.right.left = Node("F")
    return tree
