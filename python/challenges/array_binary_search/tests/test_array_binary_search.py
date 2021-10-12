from array_binary_search import __version__
from array_binary_search.array_binary_search import binarySearch

def test_version():
    assert __version__ == '0.1.0'
# test 1
def test_binarySearchCheck():
    #input array and number
    arr=[-131, -82, 0, 27, 42, 68, 179]
    n=42
    assert binarySearch(arr,n)==4
# test 2
def test_binarySearchCheck2():
    #input array and number
    arr=[4, 8, 15, 16, 23, 42]
    n=15
    assert binarySearch(arr,n)==2
# test 3
def test_binarySearchCheck3():
    #input array and number
    arr=[11, 22, 33, 44, 55, 66, 77]
    n=90
    assert binarySearch(arr,n)==-1
# test 4
def test_binarySearchCheck4():
    #input array and number
    arr=[1, 2, 3, 5, 6, 7]
    n=4
    assert binarySearch(arr,n)==-1



