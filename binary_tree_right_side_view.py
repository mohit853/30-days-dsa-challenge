# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        

        def levelOrderTraversal(node):

            if not node:
                return []

            q= deque([node])
           
            ans =[]

            while q:

                size = len(q)
               
                for i in range(size):
                    node =q.popleft()
                    if i == size -1:
                        ans.append(node.val)

                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)

            
            
            return ans

        return levelOrderTraversal(root)
            
