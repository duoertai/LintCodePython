"""
Definition of ListNode

class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""


class Solution:
    """
    @param head: The first node of the linked list.
    @return: You should return the head of the reversed linked list.
                  Reverse it in-place.
    """

    def reverse(self, head):
        # write your code here
        if head is None or head.next is None:
            return head

        prev = head
        curr = head.next
        next = head.next.next
        head.next = None

        while next is not None:
            curr.next = prev
            prev = curr
            curr = next
            next = next.next

        curr.next = prev

        return curr
