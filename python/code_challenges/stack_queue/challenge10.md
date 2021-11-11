<br>

> *[The Code .....](/python/code_challenges/stack_queue/stack_queue/stackQueue.py)*

> *[The Tests .....](/python/code_challenges/stack_queue/tests/test_stackQueue.py)*

## Stack And Queue
- Node class that has properties for the value stored in the Node, and a pointer to the next node .
- Stack class that has a top property. It creates an empty Stack when instantiated .
- Queue class that has a front property. It creates an empty Queue when instantiated .

---
## Challenge
Using a Linked List as the underlying data storage mechanism, implement both a Stack and a Queue .

---
## API
**added a method to the Queue class :**
- enqueue O(1) .
- dequeue O(1) .
- peek O(1) .
- is empty O(1) .


**added a method to the Stack class :**
- push O(1) .
- pop O(1) .
- peek O(1) .
- is empty O(1) .

---

## Tests
1. Can successfully push onto a stack . Passed ✔️
2. Can successfully push multiple values onto a stack. Passed ✔️
3. Can successfully pop off the stack. Passed ✔️
4. Can successfully empty a stack after multiple pops. Passed ✔️
5. Can successfully peek the next item on the stack . Passed ✔️
6. Can successfully instantiate an empty stack. Passed ✔️
7. Calling pop or peek on empty stack raises exception. Passed ✔️
8. Can successfully enqueue into a queue. Passed ✔️
9. Can successfully enqueue multiple values into a queue. Passed ✔️
10. Can successfully dequeue out of a queue the expected value. Passed ✔️
11. Can successfully peek into a queue, seeing the expected value. Passed ✔️
12. Can successfully empty a queue after multiple dequeues. Passed ✔️
13. Can successfully instantiate an empty queue. Passed ✔️
14. Calling dequeue or peek on empty queue raises exception. Passed ✔️
