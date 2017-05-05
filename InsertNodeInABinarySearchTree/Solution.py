"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""


class Solution:
    """
    @param root: The root of the binary search tree.
    @param node: insert this node into the binary search tree.
    @return: The root of the new binary search tree.
    """

    def insertNode(self, root, node):
        # write your code here
        if root is None:
            return node

        if node is None or root.val == node.val:
            return root

        if root.val < node.val:
            if root.right is None:
                root.right = node
                return root
            else:
                root.right = self.insertNode(root.right, node)
                return root
        else:
            if root.left is None:
                root.left = node
                return root
            else:
                root.left = self.insertNode(root.left, node)
                return root
