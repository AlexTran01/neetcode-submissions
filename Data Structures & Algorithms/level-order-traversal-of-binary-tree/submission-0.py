# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        
        res = []

        childrens = deque()
        level = deque([root])

        p2 = childrens
        p1 = level

        while True:
            level_list = []
            while p1:
                node = p1.popleft()
                if node.left:
                    p2.append(node.left)
                if node.right:
                    p2.append(node.right)
            
                level_list.append(node.val)

            res.append(level_list)
            if p2: 
                p1, p2 = p2, p1
            else: 
                break

        return res
                
