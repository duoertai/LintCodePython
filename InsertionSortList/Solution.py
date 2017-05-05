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
    @return: The head of linked list.
    """

    def insertionSortList(self, head):
        # write your code here
        if head is None or head.next is None:
            return head

        fakehead = ListNode(0)
        p = fakehead

        while head is not None:
            while p.next is not None and p.next.val < head.val:
                p = p.next

            temp = head.next
            head.next = p.next
            p.next = head
            head = temp

            p = fakehead

        return fakehead.next
