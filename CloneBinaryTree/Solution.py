"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        this.val = val
        this.left, this.right = None, None
"""
from TreeNode import TreeNode


class Solution:
    """
    @param {TreeNode} root: The root of binary tree
    @return {TreeNode} root of new tree
    """

    def cloneTree(self, root):
        # Write your code here
        if root is None:
            return None

        copy = TreeNode(root.val)
        left_copy = self.cloneTree(root.left)
        right_copy = self.cloneTree(root.right)

        copy.left = left_copy
        copy.right = right_copy

        return copy
