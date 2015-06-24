class Node :
    def __init__(self, data) :
        """
        Initializes a node with
        node value -> data
        node next pointer -> None

        """
        self.data = data
        self.next = None

    def set_data(self, data) :
        """
        Sets data value of node equal to 'data'

        """
        self.data = data

    def get_data( self ) :
        """
        Returns data value of node 

        """
        return self.data

    def set_next(self, next) :
        """
        Returns next of node to 'next'

        """
        self.next = next

    def get_next (self) :
        """
        Returns next node of the current node in the list

        """
        return self.next

class UnorderedList :

    def __init__(self ) :
        """
        Initialize an empty unordered likned list

        """
        self.head = None

    def add(self, item) :
        """
        Adds an item to linked list

        """
        new_node = Node(item)
        new_node.set_next (self.head)
        self.head = new_node

    def size(self ) :
        """
        Returns the sie of the linekd list

        """
        current = self.head
        length = 0
        while current != None :
            length += 1
            current = current.get_next()
        return length

    def search(self , item) :
        """
        Search for an 'item' in the linked list
        if found returns True otherwise False 

        """
        current = self.head
        found = False
        while current != None and not found :
            if current.get_data() == item :
                found = True
            current = current.get_next()
        return found

    def is_empty(self) :
        """
        returns 'True' if list empty 'False' otherwise 

        """
        return self.head == None

    def remove(self, item) :
        """
        removes Node with value 'item' from the list 

        """
        current = self.head
        prev = None
        found = False
        while  not found :
            if current.get_data() == item :
                found = True
            else :
                prev = current
                current = current.get_next()
        if prev == None :
            self.head = self.head.get_next()
        else :
            prev.set_next(current.get_next())

    def insert(self, index , item) :
        """
        insert a node with value item in likned list at 'index'

        """
        newnode = Node(item)
        current = self.head
        prev = None
        found = False
        count = 0
        while not found :
            if count == index :
                found = True
            else :
                prev = current
                current = current.get_next()
                count += 1
        if prev == None :
            newnode.set_next(self.head)
            self.head = newnode
        else :
            newnode.set_next(current)
            prev.set_next(newnode)

    def append(self, item) :
        """
        adds a Node with value 'item' to the end of the list

        """
        newnode = Node(item)
        current = self.head
        prev = None
        while current != None :
            prev = current
            current = current.get_next()
        prev.set_next(newnode)
        newnode.set_next(current)

    def pop(self) :
        """
        removes a node from the list and returns it's data value 

        """
        current = self.head
        prev = None
        while  current.get_next() != None :
            prev = current
            current = current.get_next()
        prev.set_next(current.get_next())
        return current.get_data()

    def pop(self, i = size(self)) :
        """
        removes a Node with inedex i and returns it's data value

        """
        current = self.head
        prev = None
        count = 0
        while count < i :
            prev = current
            current = current.get_next()
            count += 1
        if prev == None :
            self.head = self.head.get_next()
        else :
            prev.set_next(current.get_next())
        return current.get_data()

    def index(self, item) :
        """
        returns the index of node with value data value equal to item

        """
        current = self.head
        count = 0
        found = False
        while not found :
            if current.get_data() == item :
                found = True
            else :
                current = current.get_next()
                count += 1
        return count

    def print_list(self) :
        """
        prints the content of the linekd list

        """
        current = self.head
        result = " "
        while current.get_next() != None :
            result = result + str(current.get_data()) + " ----> "
            current = current.get_next()
        result += str(current.get_data())
        print result
        
    

mylist = UnorderedList()
mylist.add(31)
mylist.add(77)
mylist.add(17)
mylist.add(93)
mylist.add(26)
mylist.add(54)
mylist.print_list()
print(mylist.search(17))
print(mylist.size())
print(mylist.is_empty())
mylist.remove(17)
mylist.print_list()
mylist.insert(5, 15)
mylist.print_list()
mylist.insert(6, 17)
mylist.print_list()
mylist.insert(0, 21)
mylist.insert(3, 28)
mylist.print_list()
mylist.append(10)
mylist.print_list()
print(mylist.pop(0))
mylist.print_list()
print(mylist.pop(3))
mylist.print_list()
print(mylist.pop(7))
mylist.print_list()
print(mylist.index(28))







        
        
        
    
        
        
            

    
            

    
        

    
