# Stacks and Queues
Using a Linked List as the underlying data storage mechanism, implement both a Stack and a Queue
Stack:First input last output.
It creates an empty Stack when instantiated.

Queue:first input first output.
It creates an empty Queue when instantiated.

## Challenge
make the code clear and includes function 

## Approach & Efficiency
Stack
If you just want to add an element stack, that can be done in constant time O(1).
If you want to delete an element from stack, again constant time O(1).
BigO(n) worst case 
Queue
If you just want to add an element queue, that can be done in constant time O(1).
If you want to delete an element from queue, again constant time O(1).
BigO(n) worst case 

## API
Stack
push
tack an item and add it to the stack
pop
Removes the node from the top of the stack and if it empty return "Stack is empty"
peek
Returns: Value of the node located at the top of the stack or return "Stack is empty"
is empty
Returns: Boolean indicating whether or not the stack is empty.


Queue
enqueue
tack an item and add it to the queue
dequeue
Removes the node from the front of the queue and if it empty return "Queue is empty"
peek
Arguments: none
Returns: Value of the node located at the front of the queue or return "Queue is empty"
is empty
Returns: Boolean indicating whether or not the queue is empty.