class Stack :
    def __init__(self) :
        """
        Initialize an empty Stack
        
        """
        self.items = []

    def  is_empty(self) :
        """
        Returns 'True' if stack is empty otherwise 'False'
        
        """
        return self.items == []

    def push(self, item) :
        """
        Insert an item on Top of stack and return None
        
        """

        self.items.append(item)

    def pop(self) :
        """
        Remove an item from the Top of stack and return it 

        """
        return self.items.pop()

    def peek(self) :
        """
        Returns item present on Top of Stack

        """

        return self.items[len(self.items) - 1 ]

    def size(self) :
        """
        Returns size of the stack
        
        """
        return len(self.items)


#Tester code
s = Stack()
print(s.is_empty())
s.push(4)
s.push('dog')
print(s.peek())
s.push(True)
print(s.size())
print(s.is_empty())
s.push(8.4)
print(s.pop())
print(s.pop())
print(s.size())

