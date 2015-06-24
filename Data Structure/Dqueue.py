class Dqueue:
    
    def __init__(self) :
        """
        Initializes an empty doubly ended queue.

        """
        self.items = [ ]

    def is_empty(self) :
        """
        returns 'True' if doubly ended queue  is empty otheriwse 'False'.

        """
        return self.items == [ ]

    def add_front(self, item) :
        """
        Adds an item to front of the doubly ended queue and returns 'None'

        """
        self.items.append(item)

    def add_rear(self, item) :
        """
        Adds an item to rear of the doubly ended queue and returns 'None'

        """
        self.items.insert(0, item)

    def remove_front(self) :
        """
        Removes an item from front of the doubly ended queue and returns it

        """
        return self.items.pop()

    def remove_rear(self) :
        """
        Removes an item from front of the doubly ended queue and returns it

        """
        return self.items.pop(0)

    
