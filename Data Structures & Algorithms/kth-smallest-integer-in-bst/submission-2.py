# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        def findLeftMost(root):
            if root is None:
                return None

            leftMost = root
            ances = deque()
            while leftMost.left:
                ances.append(leftMost)
                leftMost = leftMost.left
            ances.append(leftMost)

            nonlocal k
            while ances:             
                nextSmallest = ances.pop()
                if k == 1:
                    return nextSmallest.val
                k -= 1
                if nextSmallest.right:
                    val = findLeftMost(nextSmallest.right)
                    if val: 
                        return val
                    else: 
                        pass 

            return None

        return findLeftMost(root)

        