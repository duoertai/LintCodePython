"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
from TreeNode import TreeNode


class Solution:
    """
    @param A: a list of integer
    @return: a tree node
    """

    def sortedArrayToBST(self, A):
        # write your code here
        if A is None or len(A) == 0:
            return None

        root = self.helper(A, 0, len(A) - 1)
        return root

    def helper(self, A, start, end):
        if start > end:
            return None

        mid = start + (end - start) / 2
        root = TreeNode(A[mid])
        left = self.helper(A, start, mid - 1)
        right = self.helper(A, mid + 1, end)
        root.left = left
        root.right = right

        return root
