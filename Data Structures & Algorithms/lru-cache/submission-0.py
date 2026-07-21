# from typing import Optional
# from collections import defaultdict

class Node:
    def __init__(self, value: int = -1, key: int = -1, prev: 'Node' = None, next: 'Node' = None):
        self.key = key
        self.value = value
        self.prev = prev
        self.next = next
        
        
class LRUCache:

    # n
    ## LRU: [1,2,3,4,5,6] . update 3: [1,2,4,5,6,3]

    def __init__(self, capacity: int):
        self.nodes_map = defaultdict(None)
        self.head = None # point at the start of the list / the LRU
        self.tail = None # point at the tail of the list / the MRU
        self.count = 0
        self.capacity = capacity
    

    def get(self, key: int) -> int:

        if key not in self.nodes_map:
            return -1
        
        node = self.nodes_map[key]
        val = node.value

        if self.tail == node:
            return val

        if self.head == node and node.next:
            self.head = node.next
            node.next.prev = None
            
        elif self.head != node:
            # move the node
            prev_node = node.prev
            next_node = node.next
            
            if prev_node:
                prev_node.next = next_node
            if next_node:
                next_node.prev = prev_node
        
        # put the node at the end
        self.tail.next = node
        node.prev = self.tail
        self.tail = node
        return val

    def put(self, key: int, value: int) -> None:

        if self.count == 0:
            new_node = Node(value, key)
            self.head = new_node
            self.tail = new_node
            self.nodes_map[key] = new_node
            self.count += 1
            return

        if key in self.nodes_map:
            # exist
            node = self.nodes_map[key]
            node.value = value
            
            if self.tail == node:
                return

            if self.head == node and node.next:
                self.head = node.next
                node.next.prev = None
                
            elif self.head != node:
                # move the node
                prev_node = node.prev
                next_node = node.next
                
                if prev_node:
                    prev_node.next = next_node
                if next_node:
                    next_node.prev = prev_node
            
            # put the node at the end
            self.tail.next = node
            node.prev = self.tail
            self.tail = node

        else: 
            new_node = Node(value, key)
            self.nodes_map[key] = new_node

            # put the new node and the tail.
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

            if self.count == self.capacity:
                # remove the head node, and move the head pointer
                self.nodes_map.pop(self.head.key)
                self.head = self.head.next
            else:
                self.count += 1
            


