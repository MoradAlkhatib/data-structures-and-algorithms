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
push bigO(1) for space bigO(1) for time
tack an item and add it to the stack
pop bigO(1) for space bigO(1) for time
Removes the node from the top of the stack and if it empty return "Stack is empty"
peek bigO(1) for space bigO(1) for time
Returns: Value of the node located at the top of the stack or return "Stack is empty"
is empty bigO(1) for space bigO(1) for time
Returns: Boolean indicating whether or not the stack is empty.


Queue
enqueue bigO(1) for space bigO(1) for time
tack an item and add it to the queue
dequeue bigO(1) for space bigO(1) for time
Removes the node from the front of the queue and if it empty return "Queue is empty"
peek bigO(1) for space bigO(1) for time
Arguments: none
Returns: Value of the node located at the front of the queue or return "Queue is empty"
is empty bigO(1) for space bigO(1) for time
Returns: Boolean indicating whether or not the queue is empty.