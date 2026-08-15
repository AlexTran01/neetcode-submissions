
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        n = 0
        cur = head
        while cur:
            n += 1
            cur = cur.next

        half = n//2
        p2Start = head
        while half > 0:
            p2Start = p2Start.next
            half -= 1

        nextNode = p2Start.next
        p2Start.next = None
        p2Start = nextNode

        

        prev1 = None
        while p2Start:
            nextNode = p2Start.next
            p2Start.next = prev1
            prev1 = p2Start
            p2Start = nextNode
        
        
        self.printList(prev1)
        
        # merge 2 list
        p1 = head
        p2 = prev1
        prev = dummy = ListNode()
        while p1 and p2:
            nextp2 = p2.next
            nextp1 = p1.next

            prev.next = p1
            p1.next = p2
            prev = p2

            p1 = nextp1
            p2 = nextp2
        
        if p1: 
            prev.next = p1

        self.printList(head)
        return 
  
    def printList(self, head):
        while head:
            print(head.val)
            head = head.next