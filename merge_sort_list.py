# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head or not head.next:
            return head

        mid = self.get_mid(head)
        left = head
        right = mid.next
        mid.next = None
        left_grp = self.sortList(left)
        right_grp = self.sortList(right)
        

        return self.merge(left_grp,right_grp)
    
    def merge(self,list1,list2):

        dummy = ListNode(0)
        tail = dummy


        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
                
            else:
                tail.next = list2
                list2 = list2.next
            tail  = tail.next
        
        tail.next = list1 if list1 else list2

        return dummy.next






    def get_mid(self,node):
        slow = node
        fast = node.next

        while fast and fast.next:
            slow = slow.next 
            fast = fast.next.next
        return slow
        


        
