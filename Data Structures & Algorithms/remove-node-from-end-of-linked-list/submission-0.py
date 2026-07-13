# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Reverse the List:
        prev = None
        cur = head
        while cur:
            next_node = cur.next
            cur.next = prev
            prev = cur
            cur = next_node
        
        # Reverse the List second time while searching for the nth node.
        cur = prev
        prev = None
        count = 1

        while cur:
            # skip
            if count == n:
                next_node = cur.next
                cur.next = None
                cur = next_node
                

            if not cur: 
                break

            # revese 
            next_node = cur.next
            cur.next = prev
            prev = cur
            cur = next_node
        
            count += 1

        return prev
    
        # Reverse the List:
        prev = None
        cur = head
        while cur:
            next_node = cur.next
            cur.next = prev
            prev = cur
            cur = next_node
        
        # Reverse the List second time while searching for the nth node.
        cur = prev
        prev = None
        count = 1

        while cur:
            # skip
            if count == n:
                next_node = cur.next
                prev.next = cur.next
                cur.next = None
                cur = next_node

            if not cur: 
                break

            # revese 
            next_node = cur.next
            cur.next = prev
            prev = cur
            cur = next_node

            count += 1
        return prev