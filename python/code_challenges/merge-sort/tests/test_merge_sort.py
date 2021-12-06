from merge_sort import __version__
from merge_sort.merge import merge_sort


def test_version():
    assert __version__ == '0.1.0'

def test_merge_sort():
    assert merge_sort([8,4,23,42,16,15]) == [4,8,15,16,23,42]
    #Reverse-sorted
    assert merge_sort([20,18,12,8,5,-2]) == [-2,5,8,12,18,20]
    #Few uniques
    assert merge_sort([5,12,7,5,5,7]) == [5,5,5,7,7,12]
    #Nearly-sorted
    assert merge_sort([2,3,5,7,13,11]) == [2, 3, 5, 7, 11, 13]
