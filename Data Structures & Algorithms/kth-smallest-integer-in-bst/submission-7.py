# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        res = root.val

        def dfs(root):
            nonlocal k, res
            
            if not root:
                return 
            
            dfs(root.left)
            
            if k == 0:
                return

            if k == 1:
                res = root.val
            k -= 1

            dfs(root.right)

        


        dfs(root)
        return res

        