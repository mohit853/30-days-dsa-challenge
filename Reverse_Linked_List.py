# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
     
        prev = None
        curr = head

        ## we do reveral per node 

        while curr: ## provess all nodes of linked list

            temp = curr.next
            curr.next=prev

            prev=curr
            curr=temp
        
        ## head is with prev as curr goes to null 
        return prev




        
