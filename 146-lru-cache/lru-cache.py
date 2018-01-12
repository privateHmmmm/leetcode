# -*- coding:utf-8 -*-


#
# Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and put.
#
#
#
# get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
# put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.
#
#
# Follow up:
# Could you do both operations in O(1) time complexity?
#
# Example:
#
# LRUCache cache = new LRUCache( 2 /* capacity */ );
#
# cache.put(1, 1);
# cache.put(2, 2);
# cache.get(1);       // returns 1
# cache.put(3, 3);    // evicts key 2
# cache.get(2);       // returns -1 (not found)
# cache.put(4, 4);    // evicts key 1
# cache.get(1);       // returns -1 (not found)
# cache.get(3);       // returns 3
# cache.get(4);       // returns 4
#
#


class Node(object):
    
    def __init__(self, key, value):
        
        self.key = key
        self.value = value
        self.next = None
        self.pre = None

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        
        # hashmap + double linked list
        self._map = {}
        self.head = None
        self.tail = None
        self.capacity = capacity

    def refreshNode(self, node):
        
        if node != self.tail:
            # remove from list
            if node == self.head: #!!!!
                self.head = self.head.next
            else:
                node.pre.next = node.next
                node.next.pre = node.pre
            
            # insert into tail
            self.tail.next = node
            node.pre = self.tail
            node.next = None
            self.tail = node
            
        return
    
    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        
        if key not in self._map:
            return -1
        
        self.refreshNode(self._map[key])
        return self._map[key].value
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        
        if key in self._map:
            self._map[key].value = value
            self.refreshNode(self._map[key])
        else:
            if self.capacity == 0:
                # remove head node
                del self._map[self.head.key]
                self.head = self.head.next
                self.capacity += 1
            
            # insert into one new node
            new_node = Node(key, value)
            self._map[key] = new_node
            if self.head == None:   # !!!
                self.head = new_node
            else:
                self.tail.next = new_node
                new_node.pre = self.tail
            
            self.tail = new_node
            self.capacity -=1


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
