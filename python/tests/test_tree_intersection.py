from challenges.trees.binary_tree import Node ,BinaryTree
from challenges.tree_intersection.tree_intersection import tree_intersection

def test_tree_intersection():
    
    node = Node(150)
    node.left = Node(100)
    node.left.left = Node(75)
    node.left.right = Node(160)
    node.left.right.left = Node(125)
    node.left.right.right = Node(175)
    node.right = Node(250)
    node.right.left = Node(200)
    node.right.right = Node(350)
    node.right.right.left = Node(300)
    node.right.right.right = Node(500)
    tree1 = BinaryTree()
    tree1.root = node
    
    node = Node(42)
    node.left = Node(100)
    node.left.left = Node(15)
    node.left.right = Node(160)
    node.left.right.left = Node(125)
    node.left.right.right = Node(175)
    node.right = Node(600)
    node.right.left = Node(200)
    node.right.right = Node(350)
    node.right.right.left = Node(4)
    node.right.right.right = Node(500)
    tree2 = BinaryTree()
    tree2.root = node
    assert tree_intersection(tree1,tree2) == [100, 160, 125, 175, 200, 350, 500]