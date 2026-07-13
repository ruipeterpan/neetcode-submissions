# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        cnt = 0
        ans = None

        def dfs(node):
            nonlocal cnt, ans
            if node is None:
                return
            if ans is not None:
                return
            
            dfs(node.left)

            if ans is not None:
                return
            
            cnt += 1
            if cnt == k:
                ans = node.val
                return
            
            dfs(node.right)

        dfs(root)
        return ans

        # def helper(root):
        #     if root is None:
        #         return []
        #     return helper(root.left) + [root.val] + helper(root.right)
        
        # ordered = helper(root)
        # return ordered[k - 1]