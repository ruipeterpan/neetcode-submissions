from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return []

        q = deque([root])
        # print(f"Hello! q is None? {q is None}, root type is {type(root)}")
        result = []

        while q:
            level_size = len(q)
            result_this_level = []

            for _ in range(level_size):
                curr = q.popleft()
                result_this_level.append(curr.val)

                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            
            result.append(result_this_level)
        
        return result
