import pytest
from trees.tree_max import TreesNode , MaxValue

def test_max_value(data):
    assert 11 == MaxValue(data)

@pytest.fixture
def data () :
    tree = TreesNode(2)
    tree.left = TreesNode(7)
    tree.right = TreesNode(5)
    tree.left.left = TreesNode(2)
    tree.left.right = TreesNode(6)
    tree.left.right.left = TreesNode(5)
    tree.left.right.right = TreesNode(11)
    tree.right.right = TreesNode(9)
    tree.right.right.left = TreesNode(4)
    return tree
