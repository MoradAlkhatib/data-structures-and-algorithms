import re

class Node:
    def __init__(self, value=None, next_=None):
        """
      Initalization the Node
      """
        self.value = value
        self.next = next_


class LinkedList:
    def __init__(self):
        """
        The constructor method for the linked list. Initializes the head of a linked list to None.
        """
        self.head = None

    def insert(self, value):
        """
        Take a value and store it in a Node, then insert it to the beginning of the linked list.
        """
        self.head = Node(value, self.head)


class HashTable:
    def __init__(self, size=1024):
        """
        Initialization of Hash table
        
        """
        self.__size = size
        self.__buckets = [None] * size

    def __hash(self, key):
        """
        Takes a key which is a string and returns an integer which is the index that will be used to store the key/value para in a Node at that index.
        """
        return sum([ord(char) for char in key]) * 7 % self.__size

    def add(self, key, value):
        """
        A method for adding a new value to the map
        This method should hash the key, and add the key and value pair to the table.

        Arg: Takes the key and value 
        Return : No return value
        """

        index = self.__hash(key)

        if not self.__buckets[index]:
          self.__buckets[index] = LinkedList()
        my_value = [key,value]
        self.__buckets[index].insert(my_value)
        return index
    
    def contains(self, key):
        """
        Check if a key/value pair is exists in a hashtable.
        Args:
            key (str): a key.
        Returns:
            bool: True if the key exists in the hashtable, and False otherwise.
        """
        index = self.__hash(key)
        value = self.__buckets[index]
        if value:
            if isinstance(value, LinkedList):
                current = value.head
                while current:
                    if current.value[0] == key:
                        return True
                    current = current._next
            return True
        return False

def first_repeated_word(str):
    """[tack a string and return the the word is most repeat inside the string]

    Args:
        string ([str]): [string]

    Returns:
        [str]: [word]
    """
    if str == "":
      return 'Empty String'
    strs = re.sub(r'[^\w\s]','',str).lower().split(' ')
    hash_table = HashTable()
    for i in strs:
        if hash_table.contains(i):
            return i
        else:
            hash_table.add(i,1)
    return 'Nothing Repeated ..!'
   
 