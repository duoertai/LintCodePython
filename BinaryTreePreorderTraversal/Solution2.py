"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution2:
    """
    @param root: The root of binary tree.
    @return: Preorder in ArrayList which contains node values.
    """

    def preorderTraversal(self, root):
        # write your code here
        res = []
        if root is None:
            return res

        stack = []
        stack.append(root)

        while len(stack) > 0:
            p = stack.pop()
            res.append(p.val)

            if p.right is not None:
                stack.append(p.right)

            if p.left is not None:
                stack.append(p.left)

        return res
