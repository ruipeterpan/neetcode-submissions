class Node:
    def __init__(self, val):
        self.val = val
        self.neighbors = []

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        """
        Valid tree:
        1. No cycles
        2. All nodes are connected
        """
        nodes = [Node(i) for i in range(n)]

        for a, b in edges:
            nodes[a].neighbors.append(nodes[b])
            nodes[b].neighbors.append(nodes[a])
        
        visited = set()

        def dfs(node, parent=None):
            # returns if there is a cycle in the subgraph that spans
            # out from me
            visited.add(node.val)

            for n in node.neighbors:
                if parent is not None and n == parent:
                    continue

                if n.val in visited:
                    return False

                if not dfs(n, parent=node):
                    return False
            return True
        
        if not dfs(nodes[0]):
            return False


        num_visited = len(visited)
        return num_visited == n
