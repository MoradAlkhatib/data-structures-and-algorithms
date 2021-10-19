
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
  
  def kthFromEnd(self,k):
    # function that find the element inside the linked list from the a last 
    if k<0 :
      return "Exception"
    current=self.head
    count=0
    counter=0

    while current:
      if current.next == None:
        counter =count-k
        if counter<0:
          return "Exception"
        break
      current=current.next
      count+=1

    count=0
    current=self.head
    while current:
      if count == counter:
        return current.value      
      count+=1 
      current=current.next
 

def zipLists(list1,list2):
  #this function is tack a two linked lists and return zip for its
  head_list1=list1.head
  head_list2=list2.head
  if (not head_list1) and (not head_list2):
    return "the two lists is empty"
  elif not head_list1:
    return list2.to_string()
  elif not head_list2:
    return list1.to_string()
  else:
    temp='' 
    while head_list1 and head_list2 : 
      if head_list2 : 
        temp =head_list1.next 
        head_list1.next=head_list2
        head_list1=temp 
      
      if head_list1 :
        temp =head_list2.next 
        head_list2.next=head_list1
        head_list2=temp

    return list1.to_string()



def main():
  l=LinkedList()
  l2=LinkedList()
  l.append(2)
  l.append(3)
  l.append(4)
  
  l2.append(5)
  l2.append(6)
  l2.append(7)
  l2.append(10)
  print(zipLists(l,l2))

if __name__ =="__main__":main()
 


