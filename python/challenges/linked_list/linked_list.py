
# class Node have the value and pointer of the next node
class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next


# implementation linked list
class LinkedList:
# main of linked list declare head or start point of my linked list
  def __init__(self):
    self.head = None
# add value to linked list at the beganing of it

  def insert(self, value):
    node = Node(value)
    if self.head:
      node.next = self.head
    self.head = node
  # check if the value inside linked list

  def includes(self, value):
      current = self.head
      while current:
        if current.value == value:
           return True

        else:
          current = current.next

      return False

 # print the values inside the linked list

  def to_string(self):
    str = ""
    current = self.head

    while current:
      val = current.value
      if current.next is None:
         str += "{"+f' {val} '+"}" + " -> NULL"
         break
      else:
        str += "{"+f' {val} '+"} -> "
        current = current.next
    return str

  def append(self, value):
    node = Node(value)
    current = self.head
    if current == None:
      self.head = node
      node.next = None

    while current:
      if current.next == None:
        current.next = node
        node.next = None
        break
      else:
        current = current.next


# {1}->{2}->{3}->{4}->None # 8
# {1}->{2}->{8}->{3}->{4}->None # 8,3

  def insert_before(self, target, new_value):
    """
    this function is tack two arg first for where you want to add the item before and second which item you need to add
    """
    node1=Node(target)
    if self.head is None:
      self.head = node1
      node1.next = Node(new_value)
      return
      
    if target == self.head.value:
      new_node = Node(new_value)
      new_node.next = self.head
      self.head = new_node
      return
    current = self.head
    print(current.next)
    while current.next is not None:
      if current.next.value == target:
        break
      current = current.next
      if current.next is None:
          print("item not in the list")
      else:
        new_node = Node(new_value)
        new_node.next = current.next
        current.next = new_node
 
 
     


# def insert_after(self,target,new_value):
#     """
#     this function is tack two arg first for where you want to add the item After and second which item you need to add
#     """
#     current = self.head
#     while current is not None:
#         if current.value == target:
#             break
#     current = current.next
#     if current is None:
#         print("item not in the list")
#     else:
#         new_node = Node(new_value)
#         new_node.next = current.next
#         current.next = new_node

    
