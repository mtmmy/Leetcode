import collections

class Node:
    def __init__(self, k, v):
        self.key = k
        self.val = v
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.cache = collections.OrderedDict()        

    def get(self, key):        
        """
        :type key: int
        :rtype: int
        """
        if key not in self.cache:
            return -1
        
        self.cache.move_to_end(key)
        return self.cache[key]
            
    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.cache:
            self.cache.move_to_end(key)
            self.cache[key] = value
        else:
            if len(self.cache) >= self.capacity:
                self.cache.popitem(last = False)
            self.cache[key] = value

class LRUCache2:
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.cache = dict()
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            self.add(node)
            return node.val
        return -1
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.cache:
            self.remove(self.cache[key])
        node = Node(key, value)
        self.cache[key] = node
        self.add(node)
        if len(self.cache) > self.capacity:
            node = self.head.next
            self.remove(node)
            del self.cache[node.key]

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def add(self, node):
        pTail = self.tail.prev
        pTail.next = node
        node.prev = pTail
        node.next = self.tail
        self.tail.prev = node

if __name__ == "__main__":
    target = LRUCache(2)
    target.put(1,1)
    target.put(2,2)
    print(target.get(1))
    target.put(3,3)
    print(target.get(2))
    target.put(4,4)
    print(target.get(1))
    print(target.get(3))
    print(target.get(4))