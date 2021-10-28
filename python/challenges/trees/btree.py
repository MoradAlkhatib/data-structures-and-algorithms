

"""
define a Node class that have a data, a left side and right side in the tree
"""
class Node:
    def __init__(self, data):
        self.data = data

"""
define a BinaryTree class to make a binary tree  
"""
class BinaryTree:
    def __init__(self, data):
        node=Node(data)
        self.data = node.data
        self.left = None
        self.right = None
    
    def addChild(self, data):
        """
        this function is add the number in the tree and make the small
        numbers in the left side and the bigger number in the right side.  
        """
        if data == self.data:
            return
        if data < self.data:
            if self.left:
                self.left.addChild(data)
            else:
                self.left = BinaryTree(data)
        else:
            if self.right:
                self.right.addChild(data)
            else:
                self.right = BinaryTree(data)
    
    def pre_order(self):
        """
        print the tree in the array with use depth way as a pre order.
        """
        ele = []

        ele.append(self.data)
        if self.left:
            ele += self.left.pre_order()
        
        if self.right:
            ele += self.right.pre_order()
        
        return ele

    def in_order(self):
        """
        print the tree in the array with use depth way as a In order.
        """
        ele = []
        
        if self.left:
            ele += self.left.in_order()
        ele.append(self.data)
        
        if self.right:
            ele += self.right.in_order()
        
        return ele

    def post_order(self):
        """
        print the tree in the array with use depth way as a post order.
        """
        ele = []
        
        if self.left:
            ele += self.left.post_order()
                
        if self.right:
            ele += self.right.post_order()

        ele.append(self.data)
        return ele
     
