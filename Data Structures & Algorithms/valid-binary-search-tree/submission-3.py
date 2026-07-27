# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def helper(root, lBound = float('-inf'), uBound = float('inf')):
            if root is None:
                return True
            
            if not lBound < root.val < uBound:
                return False
            
            return helper(root.left, lBound, root.val) and helper(root.right, root.val, uBound)

        return helper(root)
          
            