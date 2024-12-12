class Key:
    def __init__(self,key,value):
        self.key=key
        self.value=value


class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]
        self.occupied=0
    
    def HashTable_size(self):
        return self.size
    
    def Hash_Function(self ,key):
        return sum(ord(char) for char in key) % self.size
    
    def Hash_occupied(self):
        return self.occupied
    
    def update_key(self,key,value):
        index=self.Hash_Function(key)
        for node in self.table[index]:
            if node.key==key:
                node.value+=value
                return
        self.table[index].append(Key(key,value))
        self.occupied+=1
        if self.occupied>self.size*0.7:
            self.rehash()
    
    def search_key(self,key):
        index=self.Hash_Function(key)
        for node in self.table[index]:
            if node.key==key:
                return node.value
        return 0

    def rehash(self):
        old_table = self.table
        self.size *= 2
        self.table = [[] for _ in range(self.size)]
        self.occupied=0
        for bucket in old_table:
            for node in bucket:
                self.update_key(node.key,node.value)

    