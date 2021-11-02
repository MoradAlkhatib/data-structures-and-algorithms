from challenges.trees.binary_tree import BinarySearch 
from challenges.tree_fizz_buzz.tree_fizz_buzz import FizzBuzzTree 


    

def  test_fizz_buzz():
    tree = BinarySearch()
    tree.add(2)
    tree.add(7)
    tree.add(5)
    tree.add(9)
    tree.add(15)
    tree.add(70)
    tree.add(33)
    tree.add(30)

    print(tree.pre_order())
    # [2, 7, 5, 9, 15, 70, 33, 30]
    expected = ['2','7','Buzz','Fizz','FizzBuzz','Buzz','Fizz','FizzBuzz']
    actual = FizzBuzzTree(tree)
    assert expected == actual
    
   
    



    