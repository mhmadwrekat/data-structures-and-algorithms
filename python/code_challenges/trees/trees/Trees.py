def view():
    print('\n|------------------------------------------|')
############## NODE ###############
class Node :
    def __init__(self, value = None):
        self.value = value
        self.left = None
        self.right = None
    def __str__(self):
        return f'{self.value}'
############ Binary-Tree #############
class BinaryTree () :
    def __init__(self) :
        self.root = None
        self.output = []

    def pre_order (self) :
        output = []
        def _traveres (_root) :
            try :
                output.append(_root.value)
                if _root.left is not None :
                    _traveres(_root.left)
                if _root.right is not None :
                    _traveres(_root.right)
                return output
            except:
                return "Error"
        return _traveres

    def in_order (self) :
        def _traveres (_root) :
            try :
                output = []
                if _root :
                    output = _traveres(_root.left)
                    output.append(_root.value)
                    output = output + _traveres(_root.right)
                return output
            except:
                return "Error"
        return _traveres

    def post_order (self) :
        def _traveres (_root) :
            try :
                output = []
                if _root :
                    output = _traveres(_root.left)
                    output = output + _traveres(_root.right)
                    output.append(_root.value)
                return output
            except:
                return "Error"
        return _traveres

    def max_value (self) :
        _max = self.root.value
        def _traveres (node) :
            try :
                nonlocal _max
#                output.append(_root.value)
                if node.value > _max :
                    _max = node.value
#                    _traveres(_root.left)
                if node.left is not None :
                    _traveres(node.left)
                if node.right is not None :
                    _traveres(node.right)
            except:
                return "Error"
        _traveres(self.root)
        return _max
########## Binary-Search-Tree ###########
class BinarySearchTree (BinaryTree) :
    def add (self,data) :
        if self.root == None:
            self.root = Node(data)
        else:
            new_node = self.root
            while new_node :
                if new_node.data > data :
                      if new_node.right == None:
                        new_node.right = Node(data)
                        break
                else:
                       if new_node.left == None:
                        new_node.left = Node(data)
                        break
    def contains (self, data) :
    ## Returns : boolean
        if self.root == None :
            return 'Error'
        else:
            new_node = self.root
            while new_node :
                if new_node.data == data :
                    return True
                elif new_node.data > data :
                      if new_node.right == None :
                        return False
                else:
                       if new_node.left == None :
                         return False

def createTree () :
    tree = BinaryTree()
    tree.root = Node("A")
    tree.root.left = Node("B")
    tree.root.right = Node("C")
    tree.root.left.left = Node("D")
    tree.root.left.right = Node("E")
    tree.root.right.left = Node("F")
    return tree

def createTreeNum () :
    tree = BinaryTree()
    tree.root = Node(2)
    tree.root.left = Node(7)
    tree.root.right = Node(5)
    tree.root.left.left = Node(2)
    tree.root.left.right = Node(6)
    tree.root.left.right.left = Node(5)
    tree.root.left.right.right = Node(11)
    tree.root.right.right = Node(9)
    tree.root.right.right.left = Node(4)
    return tree

treeNum = createTreeNum()
tree_pre = createTree()
traveres_pre = tree_pre.pre_order()
traveres_in = tree_pre.in_order()
traveres_post = tree_pre.post_order()

if __name__ == "__main__" :
    view()
    print("['A', 'B', 'D', 'E', 'C', 'F'] -> Pre-Order")
    print(traveres_pre(tree_pre.root))
    view()
    print("['D', 'B', 'E', 'A', 'F', 'C'] -> In-Order")
    print(traveres_in(tree_pre.root))
    view()
    print("['D', 'E', 'B', 'F', 'C', 'A'] -> Post-Order")
    print(traveres_post(tree_pre.root))
    view()
    print('Max Value : ', treeNum.max_value())
    view()
