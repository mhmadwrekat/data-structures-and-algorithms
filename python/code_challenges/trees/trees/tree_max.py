from trees.Trees import view
class TreesNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Find the Maximum Value in a Binary Tree

def MaxValue(root):
    def inorder(tree):
        if tree:
            inorder(tree.left)
            if not (tree.val in uniques):
                uniques.add(tree.val)
            inorder(tree.right)

    uniques = set()
    inorder(root)
    array = list(uniques)

    count = 1
    if len(array) > count:
        return array[len(array) - count]
    else :
        return -1

def createTree () :
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

tree = createTree()

if __name__ == "__main__":
    view()
    print(MaxValue(tree))
    view()

