from challenges.insertion_sort.insertion_sort import insertion_sort

def test_reverse_sorted():
    arr = [15,-2,10,8,19,-6,-9]
    expected = [-9,-6,-2,8,10,15,19]
    actual = insertion_sort(arr)
    assert actual==expected


def test_few_uniques():
    arr = [5,12,7,5,5,7]
    expected = [5,5,5,7,7,12]
    actual = insertion_sort(arr)
    assert actual == expected


def test_Nearly_sorted():
    arr =  [10,5,18,2,13]
    expected = [2,5,10,13,18]
    actual = insertion_sort(arr)
    assert actual == expected