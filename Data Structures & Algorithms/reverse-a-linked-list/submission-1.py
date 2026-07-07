# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        while curr:
            next_node = curr.next # store the next node
            curr.next = prev # update the .next of current node to prev node'
            prev = curr

            # if not next_node:
            #     break

            curr = next_node # update the head -> next_node
        return prev