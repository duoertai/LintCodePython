# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from ListNode import ListNode


class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def swapPairs(self, head):
        # Write your code here
        if head is None or head.next is None:
            return head

        fakehead = ListNode(0)
        fakehead.next = head
        p = fakehead
        prev = head
        curr = head.next
        next = head.next.next

        while next is not None and next.next is not None:
            p.next = curr
            curr.next = prev
            prev.next = next

            p = prev
            prev = next
            curr = next.next
            next = next.next.next

        p.next = curr
        curr.next = prev
        prev.next = next

        return fakehead.next
