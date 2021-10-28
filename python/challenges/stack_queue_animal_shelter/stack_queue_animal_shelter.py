from challenges.stack_and_queue.queue import Queue
       


class AnimalShelter():
    """
    define a class AnimalShelter that save cats and dogs to find a  shelter for these animal. 
    """
    def __init__(self):
        self.cat = Queue()
        self.dog = Queue()

    def enqueue(self, animal):
        """
        check if the animal is cat or dog then add it to the queue. 
        """
        if animal.kind == "cat":
          self.cat.enqueue(animal.nickname)
        elif animal.kind == "dog":
          self.dog.enqueue(animal.nickname)
      
    def dequeue(self, pref):
        """
        check if the animal is cat or dog then delete the animal from queue that
         because it find how want to tack care of this animal.
        """
        if pref == "cat":
          self.cat.dequeue()
        elif pref == "dog":
          self.dog.dequeue()
        else:
          return "null"


class Cat():
  """
  define a class called Cat to made an objest for cat
  """
  def __init__(self,nickname):
    self.nickname = nickname
    self.kind = "cat"
    
class Dog():
  """
  define a class called Dog to made an objest for dog
  """
  def __init__(self,nickname):
    self.nickname = nickname
    self.kind = "dog"