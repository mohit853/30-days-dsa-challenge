# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.sum =float('-inf')
        
        def postOrder(node):
            if not node :
                return 0
            left = max(0,postOrder(node.left)) ## only include left if positive
            right = max(0,postOrder(node.right))
            
            self.sum = max(self.sum , left + right + node.val) ## subtree sum
            
            return max(left,right) + node.val
        
        postOrder(root)
        
        return self.sum
