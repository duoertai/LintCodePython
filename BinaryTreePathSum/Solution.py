"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    # @param {TreeNode} root the root of binary tree
    # @param {int} target an integer
    # @return {int[][]} all valid paths
    def binaryTreePathSum(self, root, target):
        # Write your code here
        res = []

        if root is None:
            return res

        temp = []

        self.helper(res, temp, root, target)

        return res

    def helper(self, res, temp, root, target):
        if root.left is None and root.right is None:
            if root.val == target:
                temp.append(root.val)
                line = list(temp)
                res.append(line)
                del temp[-1]
            return

        if root.left is not None:
            temp.append(root.val)
            self.helper(res, temp, root.left, target - root.val)
            del temp[-1]

        if root.right is not None:
            temp.append(root.val)
            self.helper(res, temp, root.right, target - root.val)
            del temp[-1]

        return