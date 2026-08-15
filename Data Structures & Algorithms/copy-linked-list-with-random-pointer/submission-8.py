"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self,head: 'Optional[Node]') ->'Optional[Node]':
        if head is None:
            return None
        cur = head
        while cur:
            new = Node(x = cur.val, next = cur.next, random = None)
            cur.next = new
            cur = new.next
        


        res = head.next
        cur = head
        while cur:
            cur.next.random = cur.random.next if cur.random is not None else None
            cur = cur.next.next


        cur = head
        while cur:
            nextNode = cur.next.next
            cur.next.next = nextNode.next if nextNode is not None else None
            cur.next = nextNode
            cur = nextNode
         
        return res
        
