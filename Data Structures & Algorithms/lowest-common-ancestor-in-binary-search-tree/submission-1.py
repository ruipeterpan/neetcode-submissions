# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        # TODO: reorder such that p < q
        if p.val > q.val:
            ptr = p
            p = q
            q = ptr

        if p.val < root.val < q.val:
            return root
        
        if p.val == root.val or q.val == root.val:
            return root
        
        if root.val > q.val:  # go to left subtree
            return self.lowestCommonAncestor(root.left, p, q)

        
        if root.val < p.val:
            return self.lowestCommonAncestor(root.right, p, q)