from trees import __version__
from trees.Trees import *
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
    assert data[0].root.left.value == "B"
# Test.4
def test_right_child(data) :
    assert data[0].root.right.value == "C"
# Test.5
def test_pre_order(data) :
    traveres = data[0].pre_order()
    expected = ["A","B","D","E","C","F"]
    assert traveres(data[0].root) == expected
# Test.6
def test_in_order(data) :
    traveres = data[0].in_order()
    expected = ["D","B","E","A","F","C"]
    assert traveres(data[0].root) == expected
# Test.7
def test_post_order(data) :
    traveres = data[0].post_order()
    expected = ["D","E","B","F","C","A"]
    assert traveres(data[0].root) == expected
# Test.8
def test_max_value(data):
    assert 11 == data[1].max_value()
# Test.9
def test_tree_breadth_first(data):
    treeNum = data[1].breadthFirst()
    treeStr = data[0].breadthFirst()
    assert treeNum(data[1].root) == [2, 7, 5, 2, 6, 9, 5, 11, 4]
    assert treeStr(data[0].root) == ['A', 'B', 'C', 'D', 'E', 'F']
# Test.10
def test_tree_fizz_buzz(data):
    assert FizzBuzzTree(data[1]) == ['2', '7', '2', 'Fizz', 'Buzz', '11', 'Buzz', 'Fizz', '4']
    assert FizzBuzzTree(data[2]) == ['Fizz', 'FizzBuzz', '8', 'Buzz', 'Fizz', '11', 'Buzz', 'Fizz', '4']
# Tree Data
@pytest.fixture
def data () :
    treeOne = BinaryTree()
    treeOne.root = Node("A")
    treeOne.root.left = Node("B")
    treeOne.root.right = Node("C")
    treeOne.root.left.left = Node("D")
    treeOne.root.left.right = Node("E")
    treeOne.root.right.left = Node("F")
    treeTwo = BinaryTree()
    treeTwo.root = Node(2)
    treeTwo.root.left = Node(7)
    treeTwo.root.right = Node(5)
    treeTwo.root.left.left = Node(2)
    treeTwo.root.left.right = Node(6)
    treeTwo.root.left.right.left = Node(5)
    treeTwo.root.left.right.right = Node(11)
    treeTwo.root.right.right = Node(9)
    treeTwo.root.right.right.left = Node(4)
    treeThree = BinaryTree()
    treeThree.root = Node(12)
    treeThree.root.left = Node(15)
    treeThree.root.right = Node(5)
    treeThree.root.left.right = Node(6)
    treeThree.root.left.left = Node(8)
    treeThree.root.right.right=Node(9)
    treeThree.root.right.right.left=Node(4)
    treeThree.root.left.left.right=Node(5)
    treeThree.root.left.right.left = Node(11)
    return [treeOne, treeTwo, treeThree]
