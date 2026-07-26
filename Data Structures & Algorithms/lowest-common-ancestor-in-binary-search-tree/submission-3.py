# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        ances = deque()

        def findAndUpdateQueue(node, target):
            if not node:
                return False
            elif node.val == target.val or findAndUpdateQueue(node.left, target) or findAndUpdateQueue(node.right, target):
                ances.append(node)
                return True
            else:
                return False
    
        def findNode(node, target, prev=None):
            if not node or node == prev:
                return False
            elif node.val == target.val or findNode(node.left, target, prev) or findNode(node.right, target, prev):
                return True
            else:
                return False

        findAndUpdateQueue(root, p)
        prev = None
        while ances:
            node = ances.popleft()
            if findNode(node, q, prev):
                return node
            prev = node

        return None
