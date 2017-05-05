"""
Definition of ListNode
class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""


class Solution:
    # @param node: the node in the list should be deleted
    # @return: nothing
    def deleteNode(self, node):
        # write your code here
        while node.next is not None and node.next.next is not None:
            node.val = node.next.val
            node = node.next

        node.val = node.next.val
        node.next = None

        return