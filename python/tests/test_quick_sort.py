from challenges.quick_sort.quick_sort import quick_sort
def test_reverse_sorted():
    arr = [20,18,12,8,5,-2,-3]
    expected = [-3,-2,5,8,12,18,20]
    actual = quick_sort(arr ,0 ,len(arr)-1)
    assert actual==expected


def test_few_uniques():
    arr = [5,12,7,5,5,7]
    expected = [5,5,5,7,7,12]
    actual = quick_sort(arr,0 ,len(arr)-1)
    assert actual == expected


def test_Nearly_sorted():
    arr =  [2,3,5,7,13,11]
    expected = [2,3,5,7,11,13]
    actual = quick_sort(arr,0 ,len(arr)-1)
    assert actual == expected