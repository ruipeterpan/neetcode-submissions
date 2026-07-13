# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:  # match
            if (not root.left) and (not root.right):
                return None
            elif root.left and (not root.right):  # no right children
                return root.left
            elif root.right and (not root.left):
                return root.right
            else:  # two children
                # let's say: we prompte the max val in 
                # the left subtree as new root.
                new_val = None
                new_root = root.left
                while new_root.right:
                    new_root = new_root.right
                root.val = new_root.val
                root.left = self.deleteNode(root.left, root.val)
                return root
        
        return root
