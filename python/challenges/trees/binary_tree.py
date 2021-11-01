class Node:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None
   

class BinaryTree:
    def __init__(self):
        self.root=None

    def pre_order(self):
        """
        print the tree in the array with use depth way as a pre order.
        """
        arr=[]
        def rec(node):
            if node:
                arr.append(node.value)
                if node.left:
                    rec(node.left)
                if node.right:
                    rec(node.right)
        rec(self.root)

        return arr


    def in_order(self):
        """
        print the tree in the array with use depth way as a In order.
        """
        arr=[]
        def rec(node):
            if node:               
                if node.left:
                    rec(node.left)
                arr.append(node.value)
                if node.right:
                    rec(node.right)
        rec(self.root)

        return arr

    def post_order(self):
        """
        print the tree in the array with use depth way as a post order.
        """
        arr=[]
        def rec(node):
            if node:               
                if node.left:
                    rec(node.left)
                if node.right:
                    rec(node.right)
                arr.append(node.value)
        rec(self.root)

        return arr
    
    def find_maximum_value(self):
        """
        function have no argument and return max value if the tree not empty other wise return 0 
        """
        if self.root == None:
          return 0
        maximum_value = self.root.value
        def maximum_value_fun(root):
          nonlocal maximum_value
          if root.value > maximum_value:
              maximum_value = root.value
          if root.left:
              maximum_value_fun(root.left)
          if root.right:
              maximum_value_fun(root.right)
          return maximum_value
        return maximum_value_fun(self.root)





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




class BinarySearch(BinaryTree):
    
    def bfs(self):
     """
     A binary tree method which returns a list of items that it contains
     input: None
     output: tree items
    """
     breadth = Queue()
     breadth.enqueue(self.root)

     list_of_items = []
     while breadth.peek():
        front=breadth.dequeue()
        list_of_items+=[front.value]
        if front.left:
            breadth.enqueue(front.left)
        if front.right:
            breadth.enqueue(front.right)
     return list_of_items
    

    def add(self,value):
        """
        this function is add the item in the tree and make the small
        numbers in the left side and the bigger item in the right side.  
        """
        if not self.root:
            self.root= Node(value)
        else :
            temp = self.root
            while temp:
                if value < temp.value:
                    if not temp.left:
                        temp.left = Node(value)
                        break
                    temp = temp.left
                else:
                    if not temp.right:
                        temp.right = Node(value)
                        break
                    temp = temp.right
        pass

    def __contains__(self,value):
        """
        search for a value in the tree
        input : value
        output : True/False
        """
        if not self.root:
            raise Exception("Empty Tree !!!")

        else:
            temp = self.root
            while temp:
                if temp.value == value:
                    return True
                elif temp.value > value:
                    if not temp.left:
                        return False
                    temp = temp.left
                else:
                    if not temp.right:
                        return False
                    temp = temp.right



    
    
  
        
  









        















