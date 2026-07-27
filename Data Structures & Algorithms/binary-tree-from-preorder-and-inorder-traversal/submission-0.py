# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:


        def helper(preorder, inorder):
            if len(preorder) == 0:
                return 

            parent = preorder[0]
            index = -1

            for i in range(len(inorder)):
                if inorder[i] == parent:
                    index = i

            leftTree, rightTree = None, None
            # print(parent)
            # print(preorder)
            # print(inorder)
            # print(f"leftTree: {preorder[ 1: index+1]}, {inorder[:index]}, count: {index}")
            # print(f"rightTree:{preorder[index+1: ]}, {inorder[index+1: ]}, count: {len(inorder) - 1 - index}")

            if index > 0:
                leftTree = helper(preorder[ 1: index+1], inorder[:index])
            if (len(inorder) - 1 - index) > 0:
                rightTree = helper(preorder[index+1: ], inorder[index+1: ])

            return TreeNode(parent, leftTree, rightTree)

        return helper(preorder, inorder)