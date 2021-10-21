from challenges.stack_and_queue.queue import (Queue,Node)
# Can successfully enqueue into a queue
def test_enqueue():
    q=Queue()
    q.EnQueue(5)
    assert q.front.item==5
# Can successfully enqueue multiple values into a queue
def test_multiple_enqueue():
    q=Queue()
    q.EnQueue(5)
    q.EnQueue(6)
    q.EnQueue(7)
    assert q.front.item==5
    assert q.rear.item==7
# Can successfully dequeue out of a queue the expected value
def test_dequeue():
    q=Queue()
    q.EnQueue(5)
    q.EnQueue(6)
    q.EnQueue(7)
    q.DeQueue()
    assert q.front.item==6
# Can successfully peek into a queue, seeing the expected value
def test_peek():
    q=Queue()
    q.EnQueue(5)
    q.EnQueue(6)
    q.EnQueue(7)
    assert q.peek()==5
# Can successfully empty a queue after multiple dequeues
def test_is_empty():
    q=Queue()
    q.EnQueue(5)
    q.EnQueue(6)
    q.DeQueue()
    q.DeQueue()
    assert q.isEmpty()==True
# Can successfully instantiate an empty queue
def test_empty():
    q=Queue()
    assert q.isEmpty()==True
# Calling dequeue or peek on empty queue raises exception
def test_dequeue_or_peek_on_empty():
    q=Queue()
    assert q.peek()=="Queue is empty"
    assert q.DeQueue()=="Queue is empty"