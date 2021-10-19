
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

  def append(self, new_value):
    # add and items to linked list in tha last postion
    new_node = Node(new_value)
    if self.head is None:
      self.head = new_node
      return
 
    last = self.head
    while last.next:
      last = last.next
    last.next = new_node



  def insert_before(self, target, new_value):
    """
    this function is tack two arg first for where you want to add the item before and second which item you need to add
    """
    current=self.head
    if self.head==None:
      self.insert(new_value)
    else:
      while current:
        if self.head.next.value==target:
          data_after=current.next
          current.next=Node(new_value)
          current.next.next=data_after
          break
        current=current.next 
   
 
 
  def insert_after(self,value,new_data):
    """
    this function is tack two arg first for where you want to add the item After and second which item you need to add
    """
    current=self.head
    while current:
      if current.value==value:
        next_data=current.next
        current.next=Node(new_data)
        Node(new_data).next=next_data
        break
      current=current.next    
  

 


  
 


