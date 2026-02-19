# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root:
            return 0
        

        ans = []
        def avg(level):
            return sum(level) / len(level)

        def levelOrder(node):


           
            q= deque([node])

            while q:
                si = len(q)
                
                level_sum =0
                for _ in range(si):

                    node = q.popleft()
                    level_sum += node.val

                    if node.left:
                        q.append(node.left)
                    
                    if node.right:
                        q.append(node.right)
                
                avg_per_level = level_sum / si
                ans.append(avg_per_level)
        
        levelOrder(root)
        return ans

