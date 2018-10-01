# [146. LRU Cache](https://leetcode.com/problems/lru-cache)

## Description

Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and put.

get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.

Follow up:
Could you do both operations in O(1) time complexity?

Example:

```
LRUCache cache = new LRUCache( 2 /* capacity */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // returns 1
cache.put(3, 3);    // evicts key 2
cache.get(2);       // returns -1 (not found)
cache.put(4, 4);    // evicts key 1
cache.get(1);       // returns -1 (not found)
cache.get(3);       // returns 3
cache.get(4);       // returns 4
```



## Solution

When the cache reaches its capacity, we have to remove the one which is least recently used item. In the solution, we use ordered dictionary which helps us to keep the order of entries.

For get function, when a key has been accessed, we move it to the end of the dictionary. The purpose of this movement is that we can keep the least recently used item at the top of the dictionary so that we can remove it easily.

For put function, if key already exists, we update its value and move it to the end. Otherwise, we need to check the capacity. If there is still room in the cache, we simply add the data. Otherwise, we pop the top item of the dictionary which is our least recently used item and put the new one.

The accessing time of the dictionary is O(1). Hence the operation of get and put are both O(1).
