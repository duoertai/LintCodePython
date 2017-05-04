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
    @return: Postorder in ArrayList which contains node values.
    """

    def postorderTraversal(self, root):
        # write your code herehttps://www.lintcode.com/en/problem/binary-tree-postorder-traversal/#
        res = []
        if root is None:
            return res

        self.helper(res, root)

        return res

    def helper(self, res, root):
        if root is None:
            return

        self.helper(res, root.left)
        self.helper(res, root.right)
        res.append(root.val)

        return
