from linked_list import __version__
from linked_list.linked import LinkedList
import pytest

def test_version():
    assert __version__ == '0.1.0'

def test_version():
    assert __version__ == '0.1.0'

def test_empty_linked_list():
    ll = LinkedList()
    actual = ll.head
    expected = None
    assert expected == actual

def test_insert_linked_list():
    ll = LinkedList()
    ll.insert('value01')
    actual = ll.__str__()
    expected = '{value01}->None'
    assert expected == actual

def test_incude_linked_list():
    ll = LinkedList()
    ll.append('value01')
    actual = ll.includes('value01')
    expected = True
    assert actual == expected

def test_insert_before():
    ll = LinkedList()
    # ll.append('value01')
    ll.append('value012')
    ll.append('value022')
    ll.append('value033')
    ll.insert_before("value022",'value077s')
    actual = ll.__str__()
    expexted = "{value012}->{value077s}->{value022}->{value033}->None"
    assert expexted == actual

def test_insert_After():
    ll = LinkedList()
    # ll.append('value01')
    ll.append('value012')
    ll.append('value022')
    ll.append('value033')
    ll.insert_Aftre("value022",'value077s')
    actual = ll.__str__()
    expexted = "{value012}->{value022}->{value077s}->{value033}->None"
    assert expexted == actual

def test_kthFromEnd():
    ll = LinkedList()
    ll.append('value012')
    ll.append('value022')
    ll.append('value033')
    actual = ll.kthFromEnd(0)
    expected = 'value033'
    assert actual == expected

@pytest.fixture
def data():
    ll = LinkedList()
    return data
