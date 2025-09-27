

""" Node is defined as
class node:
  def __init__(self, data):
      self.data = data
      self.left = None
      self.right = None
"""
def check_binary_search_tree_(root):
    def helper(root,min_val,max_val):
        if root is None:
            return True
    
        if not min_val < root.data < max_val:
            return False
        is_left =  helper(root.left,min_val,root.data)
        
        is_right =  helper(root.right,root.data,max_val)
        
        return is_left and is_right
    
    return helper(root,float('-inf'), float('inf'))
    
