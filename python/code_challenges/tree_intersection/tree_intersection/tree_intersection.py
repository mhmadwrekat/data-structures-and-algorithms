class Node :
    def __init__(self, value = None) :
        self.value = value
        self.left = None
        self.right = None

    def __str__(self) :
        return str(self.value)

class binary_tree :
    def __init__(self, root = None) :
        self.root = root

    def pre_order(self) :
        pre_order_output = []
        if self.root == None :
            return pre_order_output
        def walk(root) :
            pre_order_output.append(root.value)
            if root.left :
                walk(root.left)
            if root.right :
                walk(root.right)
        walk(self.root)
        return pre_order_output

def tree_intersection(tree_one, tree_two) :
      output = []
      if tree_one.root == None or tree_two.root == None :
        return None
      def walk(root_one, root_two) :
        if root_one.value == root_two.value :
          output.append(root_one.value)
        if root_one.left and root_two.left :
          walk(root_one.left, root_two.left)
        if root_one.right and root_two.right :
          walk(root_one.right, root_two.right)
      walk(tree_one.root, tree_two.root)
      return output

