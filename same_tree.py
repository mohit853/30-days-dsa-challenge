# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        def preOrder(p,q):
            if not p and not q:
                return True
            if not p or not q:
                return False
            ## root
            if p.val != q.val:
                return False

            ## left
            is_left=preOrder(p.left, q.left)
            ## right
            is_right=preOrder(p.right, q.right)

            return is_left and is_right





        return preOrder(p,q)
        
