
from challenges.stack_and_queue.stack import Stack

def validate_brackets(val_str):
    """
    function that tack an string and check if it have a validate brackets
    ever open bracket must have a close bracket from same type of bracket
    """
    stack=Stack()
    for i in val_str:
        if i=="{" or i=="[" or i=="(":
            stack.push(i)
        elif i=="}":
            if stack.peek()=="{":
                stack.pop()
            else:
                return False
        elif i=="]":
            if stack.peek()=="[":
                stack.pop()
            else:
                return False
        elif i==")":
            if stack.peek()=="(":
                stack.pop()
            else:
                return False
    if stack.top:
        return False
    else:
        return True



