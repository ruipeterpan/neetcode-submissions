# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        return self.goodNodesHelper(root, curr_max=root.val)

    def goodNodesHelper(self, node, curr_max):
        if node is None:
            return 0
        
        base = 0 if node.val < curr_max else 1
        
        left = self.goodNodesHelper(node.left, max(curr_max, node.val))
        right = self.goodNodesHelper(node.right, max(curr_max, node.val))

        # print(f"Checking node {node.val}, curr_max {curr_max}, left {left}, right {right}, this {base}")

        return base + left + right
