

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
    
    # def search(self, data):
    #     if data == self.data:
    #         return True
    #     if data < self.data:
    #         if self.left:
    #             return self.left.search(data)
    #         else:
    #             return False
    #     else:
    #         if self.right:
    #             return self.right.search(data)
    #         else:
    #             return False
    
    # def find_min(self):
    #     if self.left is None:
    #         return self.data
    #     return self.left.find_min()
    
    # def find_max(self):
    #     if self.right is None:
    #         return self.data
    #     return self.right.find_max()
    
    # def delete(self, val):
    #     if val < self.data:
    #         if self.left:
    #             self.left = self.left.delete(val)
    #     elif val > self.data:
    #         if self.right:
    #             self.right = self.right.delete(val)
    #     else:
    #         if self.left is None and self.right is None:
    #             return None
    #         if self.left is None:
    #             return self.right
    #         if self.right is None:
    #             return self.left
            
    #         min_val = self.right.find_min()
    #         self.data = min_val
    #         self.right = self.right.delete(val)
        
    #     return self



def build(element):
    root = BinaryTree(element[0])
    for i in range(1,len(element)):
        root.addChild(element[i])
    return root

if __name__ == '__main__':
    element = [32, 89, 12, 94, 23, 61, 2]
    tree = build(element)
    # print(tree.in_order())
    # print(tree.search(62))
    # print(tree.find_min())
    # print(tree.find_max())
    # tree.delete(12)
    print(tree.in_order())
    print(tree.pre_order())
    print(tree.post_order())