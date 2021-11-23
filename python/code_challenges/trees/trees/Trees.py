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

    def breadthFirst(self) :
        node_list=[]
        def _traveres (_root) :
            try :
                nonlocal node_list
                if _root is not None :
                    tree_list = []
                    tree_list += [_root]
                while tree_list :
                    our_Node = tree_list[0]
                    if our_Node.left :
                        tree_list += [our_Node.left]
                    if our_Node.right :
                        tree_list += [our_Node.right]
                    node_list += [tree_list.pop(0).value]
                return node_list
            except:
                return "Error"
        return _traveres

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
############ Fizz Buzz #############
def fizzBuzz(node):
    if node.value % 15 == 0:
        return'FizzBuzz'
    elif node.value %3 == 0:
        return'Fizz'
    elif node.value % 5 == 0:
        return'Buzz'
    else:
        return str(node.value)
########## Fizz Buzz Tree ###########
def FizzBuzzTree(tree):
    if not tree.root:
        return []
    new_binary_tree = BinaryTree()
    def traverser(node):
        new_binary_tree.output = new_binary_tree.output + [fizzBuzz(node)]
        if node.left:
            traverser(node.left)
        if node.right:
            traverser(node.right)
        return new_binary_tree.output
    return traverser(tree.root)

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

def createTreeNumTwo () :
    tree = BinaryTree()
    tree.root = Node(12)
    tree.root.left = Node(15)
    tree.root.right = Node(5)
    tree.root.left.right = Node(6)
    tree.root.left.left = Node(8)
    tree.root.right.right=Node(9)
    tree.root.right.right.left=Node(4)
    tree.root.left.left.right=Node(5)
    tree.root.left.right.left = Node(11)
    return tree

tree = createTree()
traveres_pre = tree.pre_order()
traveres_in = tree.in_order()
traveres_post = tree.post_order()

treeNum = createTreeNum()
treeNumPre = treeNum.breadthFirst()

treeNumTwo = createTreeNumTwo()

if __name__ == "__main__" :
    view()
    print("['A', 'B', 'D', 'E', 'C', 'F'] -> Pre-Order")
    print(traveres_pre(tree.root))
    view()
    print("['D', 'B', 'E', 'A', 'F', 'C'] -> In-Order")
    print(traveres_in(tree.root))
    view()
    print("['D', 'E', 'B', 'F', 'C', 'A'] -> Post-Order")
    print(traveres_post(tree.root))
    view()
    print('Max Value : ', treeNum.max_value())
    view()
    print('Tree Breadth First\n( expected ) [2, 7, 5, 2, 6, 9, 5, 11, 4]')
    print(' ( Actual ) ',treeNumPre(treeNum.root))
    view()
    view()
    print('( expected )')
    print("['Fizz', 'FizzBuzz', '8', 'Buzz', 'Fizz', '11', 'Buzz', 'Fizz', '4']")
    print(' ( Actual )')
    print(FizzBuzzTree(treeNumTwo))
    view()
