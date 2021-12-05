from insertion_sort import __version__
from insertion_sort.sort import insert_sort

def test_version() :
    assert __version__ == '0.1.0'

def test_insert() :
    data = [8, 4, 23, 42, 16, 15]
    actual = insert_sort(data)
    expected = [4, 8, 15, 16, 23, 42]
    assert actual == expected

def test_sort_one() :
    data = [20, 18, 12, 8, 5, -2]
    actual = insert_sort(data)
    expected = [-2, 5, 8, 12, 18, 20]
    assert actual == expected

def test_sort_two() :
    data = [5, 12, 7, 5, 5, 7]
    actual = insert_sort(data)
    expected = [5, 5, 5, 7, 7, 12]
    assert actual == expected

def test_sort_three() :
    data = [2, 3, 5, 7, 13, 11]
    actual = insert_sort(data)
    expected = [2, 3, 5, 7, 11, 13]
    assert actual == expected
