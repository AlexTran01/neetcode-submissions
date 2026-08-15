"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList1(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head: 
            return head

        hashmap = defaultdict(None)
        
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
                pass
            else: 
                newNodeRandom = Node(cur.random.val)
                hashmap[cur.random] = newNodeRandom
                newNode.random = newNodeRandom
            
            prev = newNode
            cur = cur.next

        return dummy.next

    def printList(self, head):
        while head:
            print(head.val)
            head = head.next

    def copyRandomList(self,head: 'Optional[Node]') ->'Optional[Node]':
        if head is None:
            return None
        cur = head
        while cur:
            new = Node(x = cur.val, next = cur.next, random = None)
            cur.next = new
            cur = new.next
        
        # self.printList(head)

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
        
