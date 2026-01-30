"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        
        head = root ### bring parent to next level
        while head:
            dummy = Node(0)
            sibling = dummy
            parent = head ## parent per subtree at each level
        
        
            while parent:

                if parent.left:
                    sibling.next = parent.left
                    sibling = sibling.next

                if parent.right:
                    sibling.next = parent.right
                    sibling = sibling.next

                parent = parent.next
            head = dummy.next
        
        return root
