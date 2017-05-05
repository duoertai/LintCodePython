"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
"""


class Solution:
    # @param root: a TreeNode, the root of the binary tree
    # @return: nothing
    def flatten(self, root):
        # write your code here
        if root is None:
            return

        self.flatten(root.left)
        self.flatten(root.right)

        left = root.left
        right = root.right
        root.left = None
        root.right = left

        p = root
        while p.right is not None:
            p = p.right

        p.right = right

        return