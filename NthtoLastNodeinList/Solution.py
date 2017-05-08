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
    @return: Nth to last node of a singly linked list.
    """

    def nthToLast(self, head, n):
        # write your code here
        p1 = head
        for i in range(0, n):
            p1 = p1.next

        p2 = head

        while p1 is not None:
            p1 = p1.next
            p2 = p2.next

        return p2
