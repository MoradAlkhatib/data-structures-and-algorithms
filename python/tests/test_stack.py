from challenges.stack_and_queue.stack import (Stack,Node)

# Can successfully push onto a stack
def test_push():
    s=Stack()
    s.push(5)
    assert s.top.item==5

# Can successfully push multiple values onto a stack
def test_multiple_push():
    s=Stack()
    s.push(5)
    s.push(6)
    s.push(7)
    assert s.top.item==7
# Can successfully pop off the stack
def test_pop():
    s=Stack()
    s.push(5)
    s.push(6)
    s.push(7)
    s.pop()
    assert s.top.item==6
# Can successfully empty a stack after multiple pops
def test_multiple_pop():
    s=Stack()
    s.push(5)
    s.push(6)
    s.push(7)
    s.pop()
    s.pop()
    s.pop()
    assert s.isempty()==True
# Can successfully peek the next item on the stack
def test_peek():
    s=Stack()
    s.push(5)
    s.push(6)
    assert s.peek()==6

# Can successfully instantiate an empty stack
def test_empty_stack():
    s=Stack()
    assert s.isempty()==True
# Calling pop or peek on empty stack raises exception

def test_pop_or_peek_on_empty():
    s=Stack()
    assert s.peek()=="Stack is empty"
    assert s.pop()=="Stack is empty"