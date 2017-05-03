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
    @return: Inorder in ArrayList which contains node values.
    """

    def inorderTraversal(self, root):
        # write your code here
        res = []

        if root is None:
            return res

        stack = []
        p = root

        while p is not None:
            stack.append(p)
            p = p.left

        while len(stack) > 0:
            p = stack.pop()
            res.append(p.val)

            if p.right is not None:
                p = p.right
                while p is not None:
                    stack.append(p)
                    p = p.left

        return res
