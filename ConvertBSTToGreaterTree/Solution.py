"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    # @param {TreeNode} root the root of binary tree
    # @return {TreeNode} the new root
    def convertBST(self, root):
        # Write your code here
        if root is None:
            return None

        sum = num(0)
        self.helper(root, sum)

        return root

    def helper(self, root, sum):
        if root is None:
            return

        self.helper(root.right, sum)
        root.val += sum.n
        sum.n = root.val
        self.helper(root.left, sum)

        return


class num:
    def __init__(self, n):
        self.n = n
