# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        
        data_list = []

        def serialize_helper(node):
            if node is None:
                data_list.append("#")
                return

            # preorder means: root first
            data_list.append(str(node.val))
            serialize_helper(node.left)
            serialize_helper(node.right)
        
        serialize_helper(root)


        return ','.join(data_list)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        data = data.split(',')

        def deserialize_helper(tokens):
            first = tokens[0]
            rest = tokens[1:]

            if first == "#":
                return None, rest

            root = TreeNode(int(first))

            root.left, rest = deserialize_helper(rest)
            root.right, rest = deserialize_helper(rest)

            return root, rest
        
        root, _ = deserialize_helper(data)
        return root
