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
    
        def findNode(node, target):
            if not node:
                return False
            elif node.val == target.val or findNode(node.left, target) or findNode(node.right, target):
                return True
            else:
                return False

        findAndUpdateQueue(root, p)

        print(ances)

        while ances:
            node = ances.popleft()
            if findNode(node, q):
                return node

        return None
