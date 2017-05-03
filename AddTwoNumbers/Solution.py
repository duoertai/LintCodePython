# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
from ListNode import ListNode


class Solution:
    # @param l1: the first list
    # @param l2: the second list
    # @return: the sum list of l1 and l2
    def addLists(self, l1, l2):
        # write your code here
        if l1 is None:
            return l2
        if l2 is None:
            return l1

        fakehead = ListNode(0)
        p = fakehead
        p1 = l1
        p2 = l2
        carry = 0

        while p1 is not None or p2 is not None:
            num1 = 0
            if p1 is not None:
                num1 = p1.val
                p1 = p1.next

            num2 = 0
            if p2 is not None:
                num2 = p2.val
                p2 = p2.next

            temp = (num1 + num2 + carry) % 10
            p.next = ListNode(temp)
            p = p.next
            carry = (num1 + num2 + carry) / 10

        if carry == 1:
            p.next = ListNode(1)

        return fakehead.next
