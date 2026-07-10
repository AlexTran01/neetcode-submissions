# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        hashmap = dict()
        cur = head
    
        while cur and cur.next:
            if cur.next in hashmap:
                return True
            else:
                hashmap[cur] = 1
            
            cur = cur.next

        return False