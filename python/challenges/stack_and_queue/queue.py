class Node:
     
    def __init__(self, item):
        self.item = item
        self.next = None
 
# A class to represent a queue
 
# The queue, front stores the front node

class Queue:
     
    def __init__(self):
        self.front = self.rear = None
 
    def isEmpty(self):
        return self.front == None
     
    # Method to add an item to the queue
    def enqueue(self, item):
        temp = Node(item)
         
        if self.rear == None:
            self.front = self.rear = temp
            return
        self.rear.next = temp
        self.rear = temp
 
    # Method to remove an item from queue
    def dequeue(self):
         
        if self.isEmpty():
            return "Queue is empty"
        temp = self.front
        self.front = temp.next
 
        if(self.front == None):
            self.rear = None

    def peek(self):
        if self.isEmpty():
            return "Queue is empty"
        else:
            return self.front.item

if __name__== '__main__':
    q = Queue()
    q.EnQueue(10)
    q.EnQueue(20)
    q.DeQueue()
    q.DeQueue()
    q.EnQueue(30)
    q.EnQueue(40)
    q.EnQueue(50)
    q.DeQueue()  
    print("Queue Front " + str(q.front.item))
    print("Queue Rear " + str(q.rear.item))