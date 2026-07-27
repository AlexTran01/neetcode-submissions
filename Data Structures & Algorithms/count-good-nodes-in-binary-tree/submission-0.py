# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        maxVal = root.val
        count = 1
        def dfs(root, maxVal):
            nonlocal count
            
            if root is None:
                return

            if root.val >= maxVal:
                count += 1
                maxVal = root.val
               
            dfs(root.left, maxVal)
            dfs(root.right, maxVal)

        dfs(root.left, maxVal)
        dfs(root.right, maxVal)

        return count
