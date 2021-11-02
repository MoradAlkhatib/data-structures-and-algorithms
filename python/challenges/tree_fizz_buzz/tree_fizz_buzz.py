class Node():
    def __init__(self, value = None , left =None , Right = None):
        self.value = value
        self.left = left
        self.right = Right

    def __str__(self):
        return str(self.value)

class binary_tree():
    def __init__(self):
        self.root = None
        self.arr = []
   
        
def fizzBuzz(node):
    if node.value % 15 == 0:
        return'FizzBuzz'
    elif node.value %3 == 0:
        return'Fizz'
    elif node.value % 5 == 0:
        return'Buzz'
    else:
        return str(node.value)

def FizzBuzzTree(tree):
    if not tree.root:
        return []
    new_binary_tree = binary_tree()
    def traverser(node):
        new_binary_tree.arr = new_binary_tree.arr + [fizzBuzz(node)]
        if node.left:           
            traverser(node.left)
        if node.right:
            traverser(node.right)
        return new_binary_tree.arr
    return traverser(tree.root) 