from challenges.linked_list.linked_list import (LinkedList,Node)



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