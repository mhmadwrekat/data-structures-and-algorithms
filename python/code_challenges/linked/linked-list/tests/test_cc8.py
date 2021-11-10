from linked_list.cc8 import Node , LinkedList
import pytest

@pytest.fixture
def data():
    listOne = LinkedList()
    listOne.append(1)
    listOne.append(3)
    listOne.append(2)
    listTwo = LinkedList()
    listTwo.append(5)
    listTwo.append(9)
    listTwo.append(4)
    return[listOne,listTwo]

def test_likedOne(data) :
    expected = 'head -> 1 -> 3 -> 2 -> None'
    actual = str(data[0])
    assert actual == expected

def test_likedTwo(data) :
    assert str(data[1]) == 'head -> 5 -> 9 -> 4 -> None'

def test_nodeValue() :
    num = Node
    assert str(num(5)) == '5'

def test_zipLists(data) :
    zipList = LinkedList()
    expected = 'head -> 1 -> 5 -> 3 -> 9 -> 2 -> 4 -> None'
    actual = str(zipList.zipLists(data[0],data[1]))
    assert actual == expected
