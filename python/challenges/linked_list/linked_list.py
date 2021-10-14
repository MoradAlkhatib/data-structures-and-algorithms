
# class Node have the value and pointer of the next node
class Node:
  def __init__(self, value,next=None):
    self.value = value
    self.next = next

      
 
        
# implementation linked list 
class LinkedList:
# main of linked list declare head or start point of my linked list
  def __init__(self):
    self.head = None
# add value to linked list at the beganing of it 
  def insert(self,value):
    node = Node(value)
    if self.head:
      node.next = self.head
    self.head = node
  # check if the value inside linked list    
  def includes(self,value):
      current=self.head
      while current:
        if current.value==value:
           return True

        else:
          current=current.next
      
      return False
 # print the values inside the linked list    
  def to_string(self):
    str = ""
    current = self.head
      
    while current:
      value = current.value
      if current.next is None:
         str +="{"+f' {value} '+"}" + " -> NULL"
         break
      else:
        str +="{"+f' {value} '+"} -> "
        current = current.next
    return str
 
 
 
          
 

    
