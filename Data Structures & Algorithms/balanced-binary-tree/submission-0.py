# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        

        def dfs(root):  # returns the height of the tree
            if not root:
                return 0
            
            l, r = dfs(root.left), dfs(root.right)

            if abs(l - r) > 1:
                return float('-inf')
            
            return max(l, r) + 1
        
        return dfs(root) >= 0