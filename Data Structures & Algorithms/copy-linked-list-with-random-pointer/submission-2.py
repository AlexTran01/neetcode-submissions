"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head: 
            return head

        hashmap = {}
        
        dummy = Node(-1)
        cur = head
        prev = dummy

        while cur:

            newNode = None

            if cur in hashmap:
                newNode = hashmap[cur]
            else:
                newNode = Node(cur.val)
                hashmap[cur] = newNode
            
            # set next of prev node
            prev.next = newNode

            # set random of current node
            if cur.random and cur.random in hashmap:
                newNode.random = hashmap[cur.random]

            elif not cur.random:
                1
            else: 
                newNodeRandom = Node(cur.random.val)
                hashmap[cur.random] = newNodeRandom
                newNode.random = newNodeRandom
            
            prev = newNode
            cur = cur.next

        return dummy.next
