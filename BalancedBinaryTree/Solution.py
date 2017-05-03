"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param root: The root of binary tree.
    @return: True if this Binary tree is Balanced, or false.
    """

    def isBalanced(self, root):
        # write your code here
        if root is None:
            return True

        if not self.isBalanced(root.left) or not self.isBalanced(root.right):
            return False

        left = self.get_depth(root.left)
        right = self.get_depth(root.right)

        return abs(left - right) <= 1

    def get_depth(self, root):
        if root is None:
            return 0

        left = self.get_depth(root.left)
        right = self.get_depth(root.right)

        return max(left, right) + 1