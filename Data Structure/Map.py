class HashTable :
    def __init__(self) :
        self.size = 11
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def put(self, key, value) :
        hash_value = self.hash_function(key, len(self.slots))

        if self.slots[hash_value] == None :
            self.slots[hash_value] = key
            self.data[hash_value] = value
        else :
            if self.slots[hash_value] == key :
                self.data[hash_value] = value
            else :
                next_slot = self.rehash(hash_value, len(self.slots))
                while self.slots[next_slot] != None and  self.slots[next_slot] != key :
                    next_slot = self.rehash( next_slot, len(self.slots))

                if self.slots[next_slot] == None :
                    self.slots[next_slot] = key
                    self.data[next_slot] = value
                else :
                    self.data[next_slot] = value

    def get(self, key) :
        start_slot = self.hash_function(key, len(self.slots))

        data = None
        found = False
        stop = False
        position = start_slot
        while self.slot[position] != None and not found and not stop :
            if self.slots[position] == key :
                found = True
                data = self.data[position]
            else :
                position = self.rehash(position, len(self.slots))
                if position == start_slot :
                    stop = True
        return data
    def __getitem__(self, key) :
        return self.get(key)

    def __setitem__(self, key, data) :
        self.put(key, data) 
        
    def hash_function(self, key, size ) :
        return key%size

    def rehash(self, old_hash , size) :
        return ( old_hash + 1 ) % size

h=HashTable()
h[54]="cat"
h[26]="dog"
h[93]="lion"
h[17]="tiger"
h[77]="bird"
h[31]="cow"
h[44]="goat"
h[55]="pig"
h[20]="chicken"
print(h.slots)
print(h.data)
        
