from challenges.tree_fizz_buzz.tree_fizz_buzz import *
import pytest


def  test_fizz_buzz():
    tree = Binary_search_tree()
    a_node = Node(3)             #        3       
    b_node = Node(6)             #  6     4    15
    c_node = Node(9)             #  9
    d_node = Node(4)              # 5
    e_node = Node(5)
    f_node = Node(15)


    a_node.child.append(b_node)
    a_node.child.append(d_node)
    b_node.child.append(c_node)
    c_node.child.append(e_node)
    a_node.child.append(f_node)
    tree.root = a_node
    expected=['Fizz', 'Fizz', '4', 'FizzBuzz', 'Fizz', 'Buzz']
    actul=fizz_buzz(tree).bfs()
    assert actul==expected


def  test_fizz_buzz2():
    tree = Binary_search_tree()
    a_node = Node(3)             #        3       
    b_node = Node(6)             #  6     4    15
    c_node = Node('9')             #  9
    d_node = Node(4)              # 5
    e_node = Node(5)
    f_node = Node(15)


    a_node.child.append(b_node)
    a_node.child.append(d_node)
    b_node.child.append(c_node)
    c_node.child.append(e_node)
    a_node.child.append(f_node)
    tree.root = a_node
    with pytest.raises(TypeError):
        fizz_buzz(tree)
    
   
    



    