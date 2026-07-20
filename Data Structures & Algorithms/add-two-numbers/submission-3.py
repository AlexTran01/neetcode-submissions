# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers (self, l1: Optional[ListNode], l2:Optional[ListNode]) -> Optional[ListNode]:
        remain = 0
        num1, num2 = l1,l2
        dummy = ListNode()
        prev = dummy

        while num1 or num2 or remain:
            val1 = num1.val if num1 else 0
            val2 = num2.val if num2 else 0

            sum =  val1 + val2 + remain

            remain = sum // 10
            newNode = ListNode(sum % 10)
            prev.next = newNode
            
            prev = newNode
            num1 = num1.next if num1 else None
            num2 = num2.next if num2 else None
        

        return dummy.next

            