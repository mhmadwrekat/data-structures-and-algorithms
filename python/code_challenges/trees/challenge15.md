# Trees

---
## Challenge

- Create a Node class that has properties for the data stored in the node, the left child node, and the right child nodes .
- Create a Binary Tree class .
- Create a Binary Search Tree class This class should be a sub-class of the Binary Tree Class .

---
## API

***Big O***
- Big O time complexity for inserting a new node is **O(n)**
- Big O time complexity for Searching for a specific node **O(n)** .
-  Big O space complexity for inserting a new node is **O(w)**, where **w** is the largest width of the tree .


> ***[The Code .....](/python/code_challenges/trees/trees/Trees.py)***

> ***[The Tests .....](/python/code_challenges/trees/tests/test_trees.py)***

---
***added a method to the Binary Tree class :***
- pre order
- in order
- post order

***added a method to the Binary Search Tree  class :***
- Add
- Contains

---
## Check List

- [x] Branch Name : Trees .
- [x] Create a Node class that has properties for the value stored in the node, the left child node, and the right child node .
- [x] Create a Binary Tree class .
- [x] Define a method for each of the depth first traversals :
     1. pre order
     2. in order
     3. post order which returns an array of the values, ordered appropriately.
- [x] Any exceptions or errors that come from your code should be semantic, capture-able errors. For example, rather than a default error thrown by your language, your code should raise/throw a custom, semantic error that describes what went wrong in calling the methods you wrote for this lab .
- [x] Create a Binary Search Tree class .
- [x] Method (Add) :
    1. Arguments: value
    2. Return: nothing
    3. Adds a new node with that value in the correct location in the binary .
    4. search tree.
- [x] Method (Contains) :
    1. Argument: value
    2. Returns: boolean indicating whether or not the value is in the tree at least once.
- [x] Test Can successfully instantiate an empty tree .
- [x] Test Can successfully instantiate a tree with a single root node .
- [x] Test Can successfully add a left child and right child to a single root node .
- [x] Test Can successfully return a collection from a preorder traversal .
- [x] Test Can successfully return a collection from an inorder traversal .
- [x] Test Can successfully return a collection from a postorder traversal .

---
