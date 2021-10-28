

"""
define a Node class that have a data, a left side and right side in the tree
"""
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

"""
define a BinaryTree class to make a binary tree  
"""
class BinaryTree:
    def __init__(self, data=None):
        node=Node(data)
        self.data = node.data
        self.left = node.left
        self.right = node.right
    
    
    
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
     



class BinarySearch(BinaryTree):

    def __init__(self, data):
        super().__init__(data)

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
                self.left = BinarySearch(data)
        else:
            if self.right:
                self.right.addChild(data)
            else:
                self.right = BinarySearch(data)


    def contains(self, data):
        """
        this function is check if the tree have this element or no and return true if it found or false if not
        """

        if data == self.data:
            return True
        if data < self.data:
            if self.left:
                if self.left.data==data:
                    return True
            else:
                return False
        else:
            if self.right:
                if self.left.data==data:
                    return True
            else:
                return False
    
def build(element):
    """
    this function is use array to make a tree
    """
    root = BinarySearch(element[0])
    for i in range(1,len(element)):
        root.addChild(element[i])
    return root  


if __name__ == '__main__':
    element = [32, 89, 12, 94, 23, 61, 2]
    tree = build(element)
    
    print(tree.in_order())
    print(tree.pre_order())
    print(tree.post_order())