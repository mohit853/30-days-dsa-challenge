# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(
        self,
        l1: Optional[ListNode],
        l2: Optional[ListNode]
    ) -> Optional[ListNode]:

        stk1, stk2 = [], []

        while l1:
            stk1.append(l1.val)
            l1 = l1.next

        while l2:
            stk2.append(l2.val)
            l2 = l2.next

        prev = None
        carry = 0

        while stk1 or stk2 or carry:
            val1 = stk1.pop() if stk1 else 0
            val2 = stk2.pop() if stk2 else 0

            total = val1 + val2 + carry
            digit = total % 10
            carry = total // 10

            curr = ListNode(digit)
            curr.next = prev
            prev = curr

        return prev
