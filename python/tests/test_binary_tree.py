from challenges.trees.binary_tree import BinarySearch ,BinaryTree


# Can successfully instantiate an empty tree
def test_tree():
    tree=BinaryTree()
    assert tree.data == None

# Can successfully instantiate a tree with a single root node
def test_tree_single_root():
    tree=BinaryTree(5)
    assert tree.data == 5

# Can successfully add a left child and right child to a single root node

def test_tree_add_left():
    tree=BinaryTree(5)
    tree.left==3
    assert tree.left == 3

def test_tree_add_right():
    tree=BinaryTree(5)
    assert tree.data == 5

# Can successfully return a collection from a preorder traversal



# Can successfully return a collection from an inorder traversal


# Can successfully return a collection from a postorder traversal