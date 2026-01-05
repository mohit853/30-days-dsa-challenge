# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        self.global_max =float('-inf')

        def get_max_sum(node):

            if not node :
                return 0
            max_left = max(get_max_sum(node.left),0)
            max_right = max(get_max_sum(node.right),0)
            
            curr_sum = max_left+ node.val + max_right

            self.global_max = max(curr_sum,self.global_max)

            return node.val + max(max_left,max_right)
        

        get_max_sum(root)
        return self.global_max

        
