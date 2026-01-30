# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        temp = root
        
        while temp :
            curr = temp.val
            
            if curr > p.val and curr >q.val:
                temp = temp.left
            elif curr <p.val and curr <q.val:
                temp = temp.right
            else:
                return temp
        return None
        
        
        
        
        
