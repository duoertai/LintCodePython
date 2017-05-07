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
    @param two ListNodes
    @return a ListNode
    """

    def mergeTwoLists(self, l1, l2):
        # write your code here
        if l1 is None:
            return l2
        if l2 is None:
            return l1

        fakehead = ListNode(0)
        p1 = l1
        p2 = l2
        p = fakehead

        while p1 is not None or p2 is not None:
            num1 = sys.maxint
            if p1 is not None:
                num1 = p1.val

            num2 = sys.maxint
            if p2 is not None:
                num2 = p2.val

            if num1 < num2:
                p.next = ListNode(num1)
                p1 = p1.next
            else:
                p.next = ListNode(num2)
                p2 = p2.next

            p = p.next

        return fakehead.next
