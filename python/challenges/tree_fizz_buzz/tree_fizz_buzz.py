class Node:
    def __init__(self, data):
        self.data = data
        self.child = []


class Queue:
    def __init__(self, collection=[]):
        self.data = collection

    def peek(self):
        if len(self.data):
            return True
        return False

    def enqueue(self, item):
        self.data.append(item)

    def dequeue(self):
        return self.data.pop(0)


class Binary_search_tree:
    def __init__(self):
        self.root = None

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
            front = breadth.dequeue()
            list_of_items += [front.data]
            if front.child:
                for item in front.child:
                    breadth.enqueue(item)
        return list_of_items


def fizz_buzz_maker(node):

    if not node.data % 5 and not node.data % 3:
        return "FizzBuzz"
    elif not node.data % 3:
        return "Fizz"
    elif not node.data % 5:
        return "Buzz"
    else:
        return str(node.data)


def fizz_buzz(tree):

    """
    A binary tree method which returns a k-tree of items 
    input: k-tree
    output: k-tree
    """
    breadth = Queue()
    breadth.enqueue(tree.root)
    while breadth.peek():
        current = breadth.dequeue()
        current.data = fizz_buzz_maker(current)
        if current.child:
            for item in current.child:
                breadth.enqueue(item)
     
    tree2 = Binary_search_tree()
    tree2 = tree
    
    return tree2