"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution1:
    """
    @param root: The root of binary tree.
    @return: Preorder in ArrayList which contains node values.
    """

    def preorderTraversal(self, root):
        # write your code here
        res = []
        if root is None:
            return res

        self.helper(res, root)

        return res

    def helper(self, res, root):
        if root is None:
            return

        res.append(root.val)
        self.helper(res, root.left)
        self.helper(res, root.right)

        return
