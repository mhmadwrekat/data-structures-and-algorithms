# Delete Line (2) And Delete Line (38) To Test .
"""
from stack_queue.stack_queue_pseudo import PseudoQueue
import pytest
# Test.1
def test_pseudo_enqueue() :
    psedo = PseudoQueue()
    psedo.StackEnqueue('401')
    actual = psedo.stackOne.top.value
    expected = '401'
    assert expected == actual
# Test.2
def test_pseudo_enqueue_multiple(data) :
    actual = data.stackOne.top.value
    expected = 'wrekat'
    assert expected == actual
# Test.3
def test_pseudo_dequeue(data) :
    data.StackDequeue()
    actual = data.stackTwo.top.value
    # expected The Top Will Be Next Value because The First Are Deleted .
    expected = 25
    assert expected == actual
# Test.4
def test_pseudo_empty_after_dequeue(data) :
    data.StackDequeue()
    data.StackDequeue()
    data.StackDequeue()
    assert data.stackOne.top == None
@pytest.fixture
def data() :
    psQueue = PseudoQueue()
    psQueue.StackEnqueue('mhmad')
    psQueue.StackEnqueue(25)
    psQueue.StackEnqueue('wrekat')
    return psQueue
##################################
"""
