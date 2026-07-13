# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        global_max = float('-inf')

        def helper(node):
            nonlocal global_max

            if node is None:
                return 0
            
            left_gain_max = max(0, helper(node.left))
            right_gain_max = max(0, helper(node.right))

            global_max = max(
                global_max,
                node.val,
                node.val + left_gain_max,
                node.val + right_gain_max,
                node.val + left_gain_max + right_gain_max,
            )

            return node.val + max(left_gain_max, right_gain_max)

        helper(root)
        return global_max

        # helper returns: for a node x, the maximum sum of a path that
        # lives in x's subtree, includes x, and has x at one endpoint.