# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_hashmap = {}
        for i, val in enumerate(inorder):
            inorder_hashmap[val] = i

        def helper(pre_l, pre_r, in_l, in_r):
            # construct a subtree where the preorder is
            # preorder[pre_l:pre_r+1], and inorder is
            # inorder[in_l:in_r+1]. Meaning,
            # indices are inclusive.

            if pre_l > pre_r or in_l > in_r:
                return None

            preorder_curr = preorder[pre_l:pre_r+1]
            inorder_curr = inorder[in_l:in_r+1]

            root_val = preorder_curr[0]
            root = TreeNode(val=root_val)
            root_idx_inorder = inorder_hashmap[root_val]

            size_left = root_idx_inorder - in_l  # 1
            size_right = in_r - in_l - size_left  # 2

            # left subtree (indices are inclusive):
            # preorder: pre_l + 1, pre_l + size_left
            # inorder: in_l, in_l + size_left

            # right subtree
            # preorder: pre_l + size_left + 1, pre_r
            # inorder: root_idx_inorder + 1, in_r
            root.left = helper(
                pre_l + 1, pre_l + size_left,
                in_l, in_l + size_left
            )

            root.right = helper(
                pre_l + size_left + 1, pre_r,
                root_idx_inorder + 1, in_r
            )

            return root


        return helper(0, len(preorder) - 1, 0, len(inorder) - 1)
        # (0, 3, 0, 3)
        
        

        


