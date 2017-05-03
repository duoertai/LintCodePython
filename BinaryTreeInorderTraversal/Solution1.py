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
    @return: Inorder in ArrayList which contains node values.
    """

    def inorderTraversal(self, root):
        # write your code here
        res = []

        if root is None:
            return res

        self.helper(res, root)

        return res

    def helper(self, res, root):
        if root is None:
            return

        self.helper(res, root.left)
        res.append(root.val)
        self.helper(res, root.right)

        return
