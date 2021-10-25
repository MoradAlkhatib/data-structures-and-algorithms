

from challenges.stack_queue_animal_shelter.stack_queue_animal_shelter import (AnimalShelter,Cat,Dog)

def test_stack_queue_animal_shelter_dog():
  animal_shelter = AnimalShelter()
  dog1 = Dog("NAbo")
  dog2 = Dog("Retch")
  dog3 = Dog("NANbo")
  animal_shelter.enqueue(dog1)
  animal_shelter.enqueue(dog2)
  animal_shelter.enqueue(dog3)
  assert animal_shelter.dog.front.item=="NAbo"
  animal_shelter.dequeue("dog")
  assert animal_shelter.dog.front.item=="Retch"

def test_stack_queue_animal_shelter_cat2():
  animal_shelter = AnimalShelter()
  cat_one = Cat("Nee")
  cat_two = Cat("Cee")
  cat_three = Cat("Cate")
  animal_shelter.enqueue(cat_one)
  animal_shelter.enqueue(cat_two)
  animal_shelter.enqueue(cat_three)
  assert animal_shelter.cat.front.item=="Nee"
  animal_shelter.dequeue("cat")
  assert animal_shelter.cat.front.item=="Cee"