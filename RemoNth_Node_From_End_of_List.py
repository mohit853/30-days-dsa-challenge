# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr= head
        total_nodes=0
        while curr:
            total_nodes+=1
            curr=curr.next
        
        n_from_first= total_nodes -n

        dummy = ListNode(0,head)
        prev= dummy

        while n_from_first>0:
            prev= prev.next
            n_from_first-=1
        curr = prev.next

        prev.next = curr.next

        return dummy.next
        
        
