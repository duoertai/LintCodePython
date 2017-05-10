"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    # @param T1, T2: The roots of binary tree.
    # @return: True if T2 is a subtree of T1, or false.
    def isSubtree(self, T1, T2):
        # write your code here
        if T2 is None:
            return True
        if T1 is None:
            return False

        if self.same(T1, T2):
            return True

        return self.isSubtree(T1.left, T2) or self.isSubtree(T1.right, T2)

    def same(self, t1, t2):
        if t1 is None and t2 is None:
            return True
        if t1 is None or t2 is None:
            return False

        if t1.val != t2.val:
            return False

        return self.same(t1.left, t2.left) and self.same(t1.right, t2.right)
