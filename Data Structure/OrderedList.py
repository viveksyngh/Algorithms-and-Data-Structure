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

class OrderedList :
    def __init__(self) :
        """
        Initialize an empty  likned list

        """
        self.head = None

    def add(self, item) :
        """
        Adds an item to linked list

        """
        newnode = Node(item)
        current = self.head
        prev = None
        stop = False
        while current != None and not stop :
            if item < current.get_data() :
                stop = True
            else :
                prev = current
                current = current.get_next()
        if prev  == None :
            newnode.set_next(self.head)
            self.head = newnode
        else :
            prev.set_next(newnode)
            newnode.set_next(current)

    def remove(self, item) :
        """
        Returns the sie of the linekd list

        """
        current = self.head
        prev = None
        stop = False
        found = False
        while not found and not stop :
            if current == None or item < current.get_data() :
                stop = True
            elif item == current.get_data() :
                found = True
            else :
                prev = current
                current = current.get_next()
        if stop == True or current == None :
            print(str(item) + " Not found ")
        elif prev == None :
            self.head = self.head.get_next()
        else :
            prev.set_next(current.get_next())

    def search(self, item) :
        """
        Search for an 'item' in the linked list
        if found returns True otherwise False 

        """
        current = self.head
        stop = False
        found = False
        while not found and not stop :
            if current == None or item < current.get_data() :
                stop = True
            elif item == current.get_data() :
                found = True
            else :
                current = current.get_next()
        return found

    def is_empty(self) :
        """
        returns 'True' if list empty 'False' otherwise 

        """
        return self.head == None

    def size(self) :
        """
        removes Node with value 'item' from the list 

        """
        current = self.head
        count = 0
        while current != None :
            count += 1
            current = current.get_next()
        return count

    def index(self, item) :
        """
        insert a node with value item in likned list at 'index'

        """
        current = self.head
        found = False
        stop = False
        count = 0
        while not found and not stop :
            if current == None or item < current.get_data() :
                stop = True
            elif current.get_data() == item :
                found = True
            else :
                current = current.get_next()
                count += 1
        return count

    def pop(self, pos) :
        """
        removes a node from the list with index 'pos' and returns it data value

        """
        current = self.head
        prev = None
        found = False
        stop = False
        count = 0
        while not found :
            if count == pos :
                found = True
            else :
                prev = current
                current = current.get_next()
                count += 1
        if prev == None :
            self.head = self.head.get_next()
        else :
            prev.set_next(current.get_next())
        return current.get_data()
            
                

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

mylist = OrderedList()
mylist.add(31)
mylist.print_list()
mylist.add(77)
mylist.add(17)
mylist.add(93)
mylist.add(26)
mylist.add(54)
mylist.print_list()
print(mylist.search(93))
print(mylist.search(17))
print(mylist.search(26))
print(mylist.search(100))
print(mylist.size())
print(mylist.index(54))
mylist.remove(26)
mylist.print_list()
print(mylist.pop(0))
mylist.print_list()
print(mylist.pop(3))
mylist.remove(24)
mylist.remove(77)
mylist.print_list()
print(mylist.pop(1))
mylist.print_list()
mylist.add(77)
mylist.print_list()

