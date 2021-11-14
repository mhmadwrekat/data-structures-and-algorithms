# Delete Line (2) And Delete Line (108) To Test .
"""
from stack_queue.stackQueue import Queue
from stack_queue.stackQueue import Stack
from stack_queue.stackQueue import Node
import pytest

# Test.1
def test_node_value() :
    num = Node
    assert str(num(5)) == '5'
# Test.2
def test_stack_push() :
    stack = Stack()
    stack.push('401')
    actual = stack.top.value
    expected = '401'
    assert expected == actual
# Test.3
def test_stack_push_multiple(dataStack) :
    actual = dataStack.top.value
    expected = 'wrekat'
    assert expected == actual
# Test.4
def test_stack_pop(dataStack) :
    actual = dataStack.pop()
    expected = 'wrekat'
    assert expected == actual
# Test.5
def test_stack_empty_after_pop() :
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.pop()
    stack.pop()
    assert stack.top == None
# Test.6
def test_peek(dataStack) :
    assert 'wrekat' == dataStack.stackPeek().value
# Test.7
def test_stack_empty() :
    stack = Stack()
    expected = True
    actual = stack.stackEmpty()
    assert expected == actual
# Test.8
def test_stack_raise_exception():
    stack = Stack()
    assert stack.stackPeek() == "Its Empty"
# Stack Data
@pytest.fixture
def dataStack() :
    stack = Stack()
    stack.push('mhmad')
    stack.push(25)
    stack.push('wrekat')
    return stack
##################################
# Test.9
def test_enqueue() :
    que = Queue()
    que.enqueue('401')
    actual = que.rear.value
    expected = '401'
    assert expected == actual
# Test.10
def test_multiple_enqueue(dataQueue) :
    assert 'wrekat' == dataQueue.rear.value
# Test.11
def test_dequeue() :
    que = Queue()
    que.enqueue(1)
    que.enqueue(2)
    que.enqueue(3)
    que.dequeue()
    assert que.front.value == 2
# Test.12
def test_queue_peek(dataQueue) :
    assert 'mhmad' == dataQueue.queuePeek().value
# Test.13
def test_empty_after_dequeue() :
    que = Queue()
    que.enqueue(1)
    que.enqueue(2)
    que.dequeue()
    que.dequeue()
    assert que.front == None
# Test.14
def test_queue_empty() :
    que = Queue()
    expected = True
    actual = que.queueEmpty()
    assert expected == actual
# Test.15
def test_queue_raise_exception():
  que = Queue()
  with pytest.raises(Exception, match ="Its Empty" ):
      que.queuePeek()
# Queue Data
@pytest.fixture
def dataQueue() :
    que = Queue()
    que.enqueue('mhmad')
    que.enqueue(25)
    que.enqueue('wrekat')
    return que
"""
