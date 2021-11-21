# The implementation of Node class, Linked list class, and Hashmap class. 
class Node:
    def __init__(self, value=None, next_=None):
        """
        Initialization the Node
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
        Takes a key which is a string and returns an integer which is the index that will be used to store the key/value pare in a Node at that index.
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

    def get(self, key):
        """
        Get the value corresponding to the key provided in the hashtable.
        Args:
            key (str): the key.
        Returns:
            any: the value stored corresponding to the key provided.
        """
        index = self.__hash(key)
        if self.__buckets[index]:
       
            linked_list = self.__buckets[index]
            current = linked_list.head
            while current:
      
                if current.value[0] == key: 
                    return current.value[1]
                current = current.next
        
        return None
    
    def contains(self, key):
        """
        Check if a key/value pair is exists in a hashtable.
        Args:
            key (str): a key.
        Returns:
            bool: True if the key exists in the hashtable, and False otherwise.
        """
        index = self.__hash(key)

        return True if self.__buckets[index] else False


      
      

      