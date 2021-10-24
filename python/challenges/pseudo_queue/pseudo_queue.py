from challenges.stack_and_queue.stack import Stack

class PseudoQueue:
  # class PseudoQueue that use two stack to implementation queue
  def __init__(self):
    self.stack_1 = Stack()
    self.stack_2 = Stack()

  def enqueue(self, value):
    # tack a value and add it to PseudoQueue
    self.stack_1.push(value)

  def dequeue(self):
    # tack a value and delete it from PseudoQueue
    if self.stack_2.isempty():
      if self.stack_1.isempty():
        raise Exception("queue is empty !")
              
      while not self.stack_1.isempty():
        last_stack_1_item = self.stack_1.pop()
        self.stack_2.push(last_stack_1_item) 

    return self.stack_2.pop()


        
    


    


        
        
        
    