# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if p.val > q.val:
            p, q = q, p
        
        def helper(node, smaller, larger):
            print(node.val)
            if node.val >= smaller.val and node.val <= larger.val:
                return node
            elif node.val < smaller.val:
                return helper(node.right, smaller, larger)
            elif node.val > larger.val:
                return helper(node.left, smaller, larger)

        return helper(root, p, q)
