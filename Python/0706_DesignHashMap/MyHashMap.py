class ListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.tableSize = 1000
        self.table = [None] * 1000

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        i = key % self.tableSize
        if self.table[i]:
            cur = self.table[i]
            while cur.next and cur.key != key:
                cur = cur.next
            if cur.key == key:
                cur.value = value
            else:
                cur.next = ListNode(key, value)
        else:
            self.table[i] = ListNode(key, value)
        

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        i = key % self.tableSize
        cur = self.table[i]
        while cur:
            if cur.key == key:
                return cur.value
            cur = cur.next
        return -1

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        i = key % self.tableSize        
        cur = pre = self.table[i]
        if not cur:
            return
        if cur.key == key:
            self.table[i] = cur.next
        else:
            cur = cur.next
            while cur:
                if cur.key == key:                    
                    pre.next = cur.next
                    break                
                cur, pre = cur.next, pre.next
        
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)