# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # if path passes through the root:
        # diameter is: length of height of left + length of height of right

        # dfs to get height of each node
        # then, make another dfs pass over all nodes and get the max.

        max_len = 0

        def height(root):
            nonlocal max_len
            if not root:
                return 0
            
            height_l, height_r = height(root.left), height(root.right)

            max_len = max(max_len, height_l + height_r)

            return max(height_l, height_r) + 1
        
        height(root)

        return max_len