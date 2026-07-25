# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        res = False
        queue = deque([root])
        
        def dfs(root, subRoot):
            if not root and not subRoot:
                return True
            if root and subRoot and root.val == subRoot.val:
                return True and dfs(root.left, subRoot.left) and dfs(root.right, subRoot.right)
            else: 
                return False
        
        while queue:
            node = queue.popleft()

            if node and node.val == subRoot.val:
                res = dfs(node, subRoot)

            if res: 
                break

            if node:
                queue.append(node.left)
                queue.append(node.right)

        return res
            

        