"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    # @param {TreeNode} root the root of the binary tree
    # @return {List[str]} all root-to-leaf paths
    def binaryTreePaths(self, root):
        # Write your code here
        res = []

        if root is None:
            return res

        self.helper(res, root, "")

        return res

    def helper(self, res, root, temp):
        if root.left is None and root.right is None:
            res.append(temp + str(root.val))
            return

        next = temp + str(root.val) + "->"

        if root.left is not None:
            self.helper(res, root.left, next)

        if root.right is not None:
            self.helper(res, root.right, next)

        return
