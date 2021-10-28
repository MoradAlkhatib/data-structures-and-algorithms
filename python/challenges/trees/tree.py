
class Node:
    def __init__(self,value,left=None,right=None):
        self.value=value
        self.left=left
        self.right=right

class BinaryTree:
    def __init__(self):
        self.root=None

    def insert(self,root,data):
       
        if self.root is None: 
            self.root = Node(data) 
        else: 
            if self.root.value < data: 
                if self.root.right is None: 
                    self.root.right = Node(data)
                else: 
                    self.insert(self.root.right, Node(data)) 
            else: 
                if self.root.left is None: 
                    self.root.left = Node(data) 
                else: 
                    self.insert(self.root.left, Node(data))
    
    def pre_order(self):
        """
        Pre-order: root >> left >> right
        """
        

    def in_order(self,roots):
        """
        In-order: left >> root >> right
        """ 
        self.root=Node(roots)
        if roots: 
            self.in_order(self.root.left) 
            print(self.root.value) 
            self.in_order(self.root.right) 

    
    def post_order(self):
        """
        Post-order: left >> right >> root
        """
        pass

    


        
if __name__=="__main__":
    tree=BinaryTree()
    tree.insert(5,6)
    tree.insert(5,4)
    tree.in_order(5)