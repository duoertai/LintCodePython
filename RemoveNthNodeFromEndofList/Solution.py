"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""


class Solution:
    """
    @param head: The first node of linked list.
    @param n: An integer.
    @return: The head of linked list.
    """

    def removeNthFromEnd(self, head, n):
        # write your code here
        fakehead = ListNode(0)
        fakehead.next = head

        p1 = fakehead
        p2 = fakehead

        for i in range(0, n + 1):
            p1 = p1.next

        while p1 is not None:
            p1 = p1.next
            p2 = p2.next

        p2.next = p2.next.next

        return fakehead.next
