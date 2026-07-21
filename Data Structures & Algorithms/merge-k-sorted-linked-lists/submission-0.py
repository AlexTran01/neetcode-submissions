class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode()
        prev = dummy

        while True:

            minNode = ListNode(float("infinity"))
            pos_minNode = -1

            for i in range(len(lists)):
                if lists[i] and lists[i].val < minNode.val:
                    minNode = lists[i]
                    pos_minNode = i
                    
            if minNode.val == float("infinity"):
                break

            lists[pos_minNode] = lists[pos_minNode].next
            
            prev.next = minNode
            prev = minNode

        return dummy.next