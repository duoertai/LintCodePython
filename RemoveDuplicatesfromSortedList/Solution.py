"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""


class Solution:
    """
    @param head: A ListNode
    @return: A ListNode
    """

    def deleteDuplicates(self, head):
        # write your code here
        if head is None or head.next is None:
            return head

        p = head

        while p.next is not None:
            if p.val != p.next.val:
                p = p.next
            else:
                p.next = p.next.next
        return head
