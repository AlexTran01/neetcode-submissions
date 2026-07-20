# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers (self, l1: Optional[ListNode], l2:Optional[ListNode]) -> Optional[ListNode]:
        remain = 0
        num1, num2 = l1,l2
        dummy = ListNode(-1)
        prev = dummy
        while num1 and num2:
            sum =  num1.val + num2.val + remain
            remain = sum // 10
            newNode = ListNode(sum % 10)
            prev.next = newNode
            
            prev = newNode
            num1, num2 = num1.next, num2.next
        
        bigger = num1 if num1 else num2

        while bigger: 
            sum = bigger.val + remain
            remain = sum // 10
            newNode = ListNode(sum % 10)
            prev.next = newNode

            prev = newNode
            bigger  = bigger.next

        if remain:
            prev.next = ListNode(remain)
            

        return dummy.next

            