from challenges.stack_and_queue.queue import Node


class Queue:
  """
  Queue Class
  """
  def __init__(self, collection=[]):
    self.data = collection

  def peek(self):
    if len(self.data):
      return True
    return False

  def enqueue(self,item):
    self.data.append(item)

  def dequeue(self):
    return self.data.pop(0)

def tree_breadth_first( tree ):
    """
    this function is tack a tree as an argument and return a list of element 
    on the breadth first way or return None if it empty
    """
    output = []
    temp = None
    queue = Queue()

    if tree.root == None:
        return 

    queue.enqueue(tree.root)
    while queue.peek():
        temp = queue.dequeue()
        output.append(temp.value)
        if temp.left:
            queue.enqueue(temp.left)
        if temp.right:
            queue.enqueue(temp.right)

    return output

