class Queue :
    def __init__(self) :
        """
        Initialises an empty Queue

        """
        self.items = []

    def is_empty(self) :
        """
        Returns 'True' if Queue is empty otherwise 'False'

        """
        return self.items == []

    def enqueue(self, item) :
        """
        Insert an item to the end of the Queue and Returns None 

        """
        self.items.append(0, item)

    def dequeue(self) :
        """
        Removes an item from the front end of Queue and Returns it

        """
        return self.items.pop()

    def size(self) :
        """
        Returns the size (number of items) of the Queue 

        """
        return len(self.items)

#Tester Code
q = Queue()
q.enqueue('hello')
q.enqueue('dog')
q.enqueue(3)
q.dequeue()
