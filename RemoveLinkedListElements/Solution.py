import  ListNode
class Solution:
    # @param head, a ListNode
    # @param val, an integer
    # @return a ListNode
    def removeElements(self, head, val):
        # Write your code here
        if head is None:
            return head

        fakehead = ListNode(0)
        fakehead.next = head

        p = fakehead
        while p.next is not None:
            while p.next is not None and p.next.val != val:
                p = p.next

            if p.next is not None:
                p.next = p.next.next

        return fakehead.next