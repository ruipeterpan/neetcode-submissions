# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def helper(root, low, high):
            if root is None:
                return True
            
            if not (low < root.val < high):
                return False
            
            return (
                helper(root.left, low, root.val) and
                helper(root.right, root.val, high)
            )
        
        return helper(root, float('-inf'), float('inf'))


        # if root.left is None and root.right is None:
        #     return True
        
        # if root.left is None:  # right is not None
        #     print(f"root.val {root.val}, root.right.val {root.right.val}")
        #     return root.val < root.right.val and self.isValidBST(root.right)
        
        # if root.right is None:
        #     return root.left.val < root.val and self.isValidBST(root.left)
        
        # return (root.left.val < root.val < root.right.val and
        #     self.isValidBST(root.left) and
        #     self.isValidBST(root.right)
        # )
        
