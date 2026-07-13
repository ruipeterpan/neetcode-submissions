# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque 

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        q = deque([(root, 0)])
        result = []
        last_recorded_depth = 0
        last_recorded_node = None

        while q:
            node, depth = q.popleft()
            print(f"Processing node {node.val}, depth {depth}")

            if depth != last_recorded_depth:
                print(f"last_recorded_depth {last_recorded_depth}, adding {last_recorded_node.val}")
                result.append(last_recorded_node.val)
            
            last_recorded_depth = depth
            last_recorded_node = node

            if node.left:
                q.append((node.left, depth+1))
            if node.right:
                q.append((node.right, depth+1))
            
            if len(q) == 0:  # last node
                result.append(node.val)
        
        return result


    
