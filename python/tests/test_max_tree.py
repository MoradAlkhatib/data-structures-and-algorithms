from challenges.trees.binary_tree import BinarySearch

def test_max_value():
   """
    Test max value with Tree have an elements 
   """
   tree = BinarySearch()
   tree.add(1)
   tree.add(2)
   tree.add(3)
   tree.add(18)
   tree.add(15)

   #output

   expected = 18
   actul=tree.find_maximum_value()

   assert expected==actul

def test_max_value2():
   """
    Test max value with Tree is empty 
   """
   tree = BinarySearch()
  
   #output

   expected = 0
   actul=tree.find_maximum_value()

   assert expected==actul