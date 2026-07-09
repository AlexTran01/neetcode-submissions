# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        prev = temp = ListNode()
        p1 = list1
        p2 = list2

        while p1 and p2:

            smaller = p1 if p1.val < p2.val else p2

            prev.next = smaller
            prev = smaller
            
            if p1.val < p2.val:
                p1 = p1.next
            else:
                p2 = p2.next

        if p1:
            prev.next = p1
        elif p2:
            prev.next = p2
        
        return temp.next
