# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def helper(root, upperBound, lowerBound):
            if root is None:
                return True

            leftCompare = True
            rightCompare = True
            if root.left and (root.left.val >= root.val or root.left.val <= lowerBound):
                leftCompare = False
            if root.right and (root.right.val <= root.val or root.right.val >= upperBound):
                rightCompare = False

            return leftCompare and rightCompare and helper(root.left, root.val, lowerBound) and helper(root.right, upperBound, root.val)
            
        return helper(root, float("infinity"), float("-infinity"))