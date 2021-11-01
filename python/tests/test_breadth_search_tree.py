from challenges.breadth_search_tree.breadth_search_tree import tree_breadth_first
from challenges.trees.binary_tree import BinaryTree , Node
import pytest

@pytest.fixture

def tree():
    tree = BinaryTree()
    a = Node("A")
    b = Node("B")
    c = Node("C")
    d = Node("D")
    e = Node("E")
    f = Node("F")
    tree.root = a
    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.left = f

    return tree


def test_tree_breadth_first(tree):
    """
    check if the breadth first work like expected
    """
    
    tree = tree_breadth_first(tree)

    # output must be like this 
    actual = ["A","B","C","D","E","F"]
    assert actual == tree


def test_tree_breadth_first_on_empty(tree):
    """
    check if the breadth first  on empty tree
    """
    tree = BinaryTree()
    check = tree_breadth_first(tree)

    # output must None
    actual = None
    assert actual == check