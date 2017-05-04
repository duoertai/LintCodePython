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
    @return: Postorder in ArrayList which contains node values.
    """

    def postorderTraversal(self, root):
        # write your code here
        res = []

        if root is None:
            return res

        stack = []
        stack.append(root)

        curr = root
        prev = None

        while len(stack) > 0:
            curr = stack[-1]

            if prev is None or prev.left == curr or prev.right == curr:
                if curr.left is not None:
                    stack.append(curr.left)
                elif curr.right is not None:
                    stack.append(curr.right)

            elif curr.left == prev:
                if curr.right is not None:
                    stack.append(curr.right)

            else:
                res.append(curr.val)
                stack.pop()

            prev = curr

        return res
