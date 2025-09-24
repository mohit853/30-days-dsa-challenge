from collections import deque
"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""
def levelOrder(root):
    #Write your code here
    
    q = deque([root])
    
    while q:
        current_node = q.popleft()
        print(current_node,end=" ")
        if current_node.left:
            q.append(current_node.left)
        if current_node.right:
            q.append(current_node.right)
        
        
    
    

