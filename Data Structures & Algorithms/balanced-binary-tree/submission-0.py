# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        if not root: 
            return True

        hLeft = 0
        hRight = 0

        if root.left:
            #get height on the left
            hLeft = self.dfs(root.left)
        if root.right:
            #get height on the right
            hRight = self.dfs(root.right)
        #compare the height:
        if abs(hLeft - hRight) > 1:
            return False
        
        return self.isBalanced(root.left) and self.isBalanced(root.right)

    def dfs(self, cur):
            if not cur:
                return 0
            
            return 1 + max(self.dfs(cur.left), self.dfs(cur.right))
        