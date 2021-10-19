from challenges.linked_list.linked_list import (LinkedList,Node,zipLists)



def test_node_has_int_data():
    # Arrange any data that you need to run your test
    expected = 1

    # Act on the subject of the test to produce some actual output
    node = Node(1)
    actual = node.value

    # Assert
    assert actual == expected

def test_node_has_str_data():
    # Arrange any data that you need to run your test
    expected = "a"

    # Act on the subject of the test to produce some actual output
    node = Node("a")
    actual = node.value

    # Assert
    assert actual == expected


def test_node_is_a_Node():
    # Arrange any data that you need to run your test
    expected = "Node"

    # Act on the subject of the test to produce some actual output
    node = Node(1)
    actual = type(node).__name__

    # Assert
    assert actual == expected

# def test_node_without_value():
#     node = Node()
#     if node==None:   
#       raise (TypeError,'error')


def test_new_linked_list_is_empty():
  expected = None

  ll = LinkedList()
  actual = ll.head

  assert actual == expected

def test_linked_list_insert():
  # Arrange
  expected = 1
  ll = LinkedList()

  # Act
  ll.insert(1)
  node = ll.head
  actual = node.value

  # Assert
  assert actual == expected

def test_linked_list_insert_twice():
  # Arrange
  expected = 0
  ll = LinkedList()

  # Act
  ll.insert(1)
  ll.insert(0)
  node = ll.head
  actual = node.value

  # Assert
  assert actual == expected
  assert ll.head.next.value == 1


def test_includes():
    
    ll=LinkedList()
    ll.insert(1)
    ll.insert(0)

    expected=True
    actually=ll.includes(1)
    assert actually==expected

def test_includes2():
    
    ll=LinkedList()
    ll.insert(1)
    ll.insert(0)

    expected=False
    actually=ll.includes(2)
    assert actually==expected

def test_toString():
    ll=LinkedList()
    ll.insert(1)
    ll.insert(2)
   
    expected= "{ 2 } -> { 1 } -> NULL"
    actul= ll.to_string()

    assert expected==actul


def test_append():
    
    ll=LinkedList()
    ll.append(1)
    ll.append(2)
    ll.append(4)
    
   
    expected= "{ 1 } -> { 2 } -> { 4 } -> NULL"
    actul= ll.to_string()

    assert expected==actul

def test_insert_before():
  ll=LinkedList()
  ll.append(3)
  ll.append(4)
  ll.insert_before(4,8)
  #output
  expected= "{ 3 } -> { 8 } -> { 4 } -> NULL"
  actual=ll.to_string()
  assert expected==actual

def test_insert_after():
  ll=LinkedList()
  ll.append(3)
  ll.append(4)
  #output
  ll.insert_after(4,8)
  expected= "{ 3 } -> { 4 } -> { 8 } -> NULL"
  actual=ll.to_string()
  assert expected==actual


def test_kthFromEnd():
  # where k is not at the end, but somewhere in the middle of the linked list
  ll=LinkedList()
  ll.append(1)
  ll.append(3)
  ll.append(8)
  ll.append(2) 
  #output
  
  expected=3
  actual=ll.kthFromEnd(2)
  assert expected==actual

def test_kthFromEnd1():
  # Where k is not a positive integer
  ll=LinkedList()
  ll.append(1)
  ll.append(3)
  ll.append(8)
  ll.append(2) 
  #output
  
  expected="Exception"
  actual=ll.kthFromEnd(-1)
  assert expected==actual



def test_kthFromEnd2():
  # Where k is greater than the length of the linked list
  ll=LinkedList()
  ll.append(1)
  ll.append(3)
  ll.append(8)
  ll.append(2) 
  #output
  
  expected="Exception"
  actual=ll.kthFromEnd(6)
  assert expected==actual


def test_kthFromEnd3():
  # Where k and the length of the list are the same
  ll=LinkedList()
  ll.append(1)
  ll.append(3)
  ll.append(8)
  ll.append(2) 
  #output
  
  expected=1
  actual=ll.kthFromEnd(3)
  assert expected==actual

def test_kthFromEnd4():
  # Where the linked list is of a size 1
  ll=LinkedList()
  ll.append(1) 
  #output
  
  expected=1
  actual=ll.kthFromEnd(0)
  assert expected==actual

def test_zipLists1():
  l=LinkedList()
  l2=LinkedList()
  assert zipLists(l,l2)=="the two lists is empty"

def test_zipLists2():
  l=LinkedList()
  l2=LinkedList()
  l.append(2)
  l.append(3)
  l.append(4)
  assert zipLists(l,l2)=='{ 2 } -> { 3 } -> { 4 } -> NULL'

def test_zipLists3():
  l=LinkedList()
  l2=LinkedList()
  l2.append(2)
  l2.append(3)
  l2.append(4)
  assert zipLists(l,l2)=='{ 2 } -> { 3 } -> { 4 } -> NULL'



def test_zipLists4():
  l=LinkedList()
  l2=LinkedList()
  l.append(2)
  l.append(3)
  l.append(4)
  
  l2.append(5)
  l2.append(6)
  l2.append(7)
  excepted='{ 2 } -> { 5 } -> { 3 } -> { 6 } -> { 4 } -> { 7 } -> NULL'
  assert excepted==zipLists(l,l2)

def test_zipLists4():
  l=LinkedList()
  l2=LinkedList()
  l.append(2)
  l.append(3)
  l.append(4)
  l.append(9)
  
  l2.append(5)
  l2.append(6)
  l2.append(7)
  
  excepted='{ 2 } -> { 5 } -> { 3 } -> { 6 } -> { 4 } -> { 7 } -> { 9 } -> NULL' 
  assert excepted==zipLists(l,l2)


def test_zipLists4():
  l=LinkedList()
  l2=LinkedList()
  l.append(2)
  l.append(3)
  l.append(4)
  
  l2.append(5)
  l2.append(6)
  l2.append(7)
  l2.append(10)
  excepted='{ 2 } -> { 5 } -> { 3 } -> { 6 } -> { 4 } -> { 7 } -> { 10 } -> NULL'
  assert excepted==zipLists(l,l2)