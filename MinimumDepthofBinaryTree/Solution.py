"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
import sys


class Solution:
    """
    @param root: The root of binary tree.
    @return: An integer
    """

    def minDepth(self, root):
        # write your code here
        if root is None:
            return 0

        if root.left is None and root.right is None:
            return 1

        num1 = sys.maxint
        if root.left is not None:
            num1 = self.minDepth(root.left)

        num2 = sys.maxint
        if root.right is not None:
            num2 = self.minDepth(root.right)

        return min(num1, num2) + 1
