# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:

        def helper(preorder, inorder):
            if not preorder or not inorder:
                return None

            parent = TreeNode(preorder[0])
            index = inorder.index(preorder[0])
            parent.left = helper(preorder[ 1: index+1], inorder[:index])
            parent.right= helper(preorder[index+1: ], inorder[index+1: ])

            return parent

        return helper(preorder, inorder)