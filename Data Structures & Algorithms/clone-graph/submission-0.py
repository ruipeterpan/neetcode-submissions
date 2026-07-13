"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # TODO: clone each node. for each node, establish its neighbors
        # First: DFS/BFS the whole graph. Establish a mapping of val: neighbors
        # have a list, len is num nodes. create all nodes first. 
        # then, make a pass to connect the neighbors
        if node is None:
            return None

        mapping = {}  # val: [pointer_to_cloned_node, list of ints of neighbors] 

        def dfs(node):
            if node.val in mapping:  # visited
                return
            
            new_node = Node(val=node.val)
            mapping[node.val] = [new_node, []]

            for n in node.neighbors:
                mapping[node.val][1].append(n.val)
                dfs(n)
        
        dfs(node)
        
        for val, (node, neighbors) in mapping.items():
            node.neighbors = [mapping[n][0] for n in neighbors]
        
        return mapping[1][0]


