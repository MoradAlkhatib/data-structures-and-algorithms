class Node:
    def __init__(self,item,next=None) :
         self.item=item
         self.next=next
# A class to represent a Stack
# The stack, last stores the front node
class Stack:
    def __init__(self):
        self.top=None

    def isempty(self):
        if self.top == None:
            return True
        else:
            return False
    # Method to add an item to the stack
    def push(self,item):
        node=Node(item)
        if self.top:
           node.next=self.top
        self.top=node
    # Method to remove an item from stack
    def pop(self):
        if not self.top:
            return "Stack is empty"
        else:
            temp = self.top
            self.top = temp.next
            temp.next = None
            return temp.item

    def peek(self):
        if self.isempty():
            return "Stack is empty"
        else:
            return self.top.item



    # def to_string(self):
    #     str = ""
    #     current = self.top

    #     while current:
    #         val = current.item
    #         if current.next is None:
    #             str += "{"+f' {val} '+"}" + " -> NULL"
    #             break
    #         else:
    #             str += "{"+f' {val} '+"} -> "
    #             current = current.next
    #     return str  




if __name__=='__main__':
    stack=Stack()
    stack.push(5)
    stack.push(5)
    stack.push(5)
    stack.push(5)
    print(stack.top.item)
