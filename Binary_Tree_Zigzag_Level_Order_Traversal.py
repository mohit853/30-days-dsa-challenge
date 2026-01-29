# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root :
            return []
        q = deque([root])
        ans=[]
        r_l = True
        while q:
            
            size = len(q)
            level=deque()
            for _ in range(size):
                
                node = q.popleft()
                
                if r_l:
                    level.append(node.val) 
                else:
                    level.appendleft(node.val)
            
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            r_l = not r_l
            ans.append(list(level))
        return ans
