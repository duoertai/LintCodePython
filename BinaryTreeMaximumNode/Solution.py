class Solution:
    # @param {TreeNode} root the root of binary tree
    # @return {TreeNode} the max node
    def maxNode(self, root):
        # Write your code here
        if root is None:
            return None

        if root.left is None and root.right is None:
            return root

        left_max = self.maxNode(root.left)
        right_max = self.maxNode(root.right)
        res = root

        if left_max is not None and left_max.val > res.val:
            res = left_max

        if right_max is not None and right_max.val > res.val:
            res = right_max

        return res