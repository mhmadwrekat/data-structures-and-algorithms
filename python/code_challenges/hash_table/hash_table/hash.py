

class Node :
    def __init__(self, key, value) :
        self.key = key
        self.value = value
        self.next = None

class Hashtable :
    def __init__(self) :
        self.size = 0
        self.capacity = 1024
        self.buckets = [None] * self.capacity

    def hash(self, key) :
        asscii_sum = 0
        for i in key :
            asscii_ch = ord(i)
            asscii_sum += asscii_ch
        temp_value = asscii_sum * 19
        hashed = temp_value % self.capacity
        return hashed

    def add(self, key, value) :
        self.size += 1
        index = self.hash(key)
        node = self.buckets[index]

        if node is None :
           self.buckets[index] = Node(key, value)
           return

        else:  # Collision
            prev = node
            while node is not None :
                prev = node
                node = node.next
            prev.next = Node(key, value)

    def get(self, key) :
        index = self.hash(key)
        node = self.buckets[index]
        while node is not None and node.key != key :
            node = node.next
        if node is None :
            return "NULL"
        else :
            return node.value

    def contain(self, key) :
        index = self.hash(key)
        node = self.buckets[index]
        while node is not None and node.key != key :
            node = node.next
        if node is None :
            return False
        else :
            return True

if __name__ == "__main__" :
    hash = Hashtable()

    print(hash.hash('Wrekat'))
    print(hash.hash('takerW'))
