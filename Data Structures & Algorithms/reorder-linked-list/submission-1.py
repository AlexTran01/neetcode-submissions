
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
       # get the length:
        n = 0
        cur = head
        while cur:
            n += 1
            cur = cur.next

        if n == 1:
            return 
        # print(f"length : {n}")

        
        # split in halfs, O()
        cur = head
        for i in range(n // 2):
            if i == (n // 2) - 1:
                nextNode = cur.next
                cur.next = None
                cur = nextNode
            else:
                cur = cur.next

        # print(f"2nd list head: {cur}, {cur.val if cur else -1}")

        # reverse the second list
        # cur = head of second List
        prev = None # will hold the head of 2nd list at the end of reverse
        while cur: 
            nextNode = cur.next
            cur.next = prev
            prev = cur
            cur = nextNode
            
        
        # print(f"2nd list head after reorder: {prev}, {prev.val if prev else -1}")


        # merge the 2 list
        l1 = head
        l2 = prev
        print(l1.val, l2.val)
        while l1 and l2:
            l1_next = l1.next
            l2_next = l2.next

            l1.next = l2

            l1 = l1_next
            if l1:
                l2.next = l1

            l2 = l2_next
    
        # l1 = l2 # last element of the 2nd list.
        return None
  