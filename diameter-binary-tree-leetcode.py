# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.dia =0
        def height(root):

            if root is None :
                return -1
            
            left_h = height(root.left)
            right_h = height(root.right)

            self.dia  = max(self.dia,left_h+right_h+2)

            return 1+ max(left_h, right_h)
        
        height(root)
        return self.dia
        
