# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode()
        prev = dummy
        l_node, r_node = head, head
        count = 0

        while l_node and r_node:
            count += 1

            if count == k:
                # store the next and after ward node
                next_right_node = r_node.next
                # before_left_node = prev

                # reverse the list
                r_node.next = None
                self.reverseList(l_node) #reverse k-node list

                # putting them back the org list
                prev.next = r_node 
                l_node.next = next_right_node
                
                # reset count and prev.
                prev = l_node
                count = 0

                # put all two pointer at the end of the reversed k-node list
                r_node = l_node.next
                l_node = l_node.next

            else:
                r_node = r_node.next
        
        return dummy.next

    def reverseList(self, head):

        prev = None

        while head:
            next_node = head.next

            head.next = prev

            prev = head
            head = next_node

        return prev