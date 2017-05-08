"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
from ListNode import ListNode


class Solution:
    """
    @param head: The first node of linked list.
    @param x: an integer
    @return: a ListNode
    """

    def partition(self, head, x):
        # write your code here
        if head is None or head.next is None:
            return head

        fakehead1 = ListNode(0)
        fakehead2 = ListNode(0)
        p1 = fakehead1
        p2 = fakehead2
        p = head

        while p is not None:
            if p.val < x:
                p1.next = ListNode(p.val)
                p1 = p1.next
            else:
                p2.next = ListNode(p.val)
                p2 = p2.next

            p = p.next

        p1.next = fakehead2.next

        return fakehead1.next
