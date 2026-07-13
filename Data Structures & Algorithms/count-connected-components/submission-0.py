class Node:
    def __init__(self, val):
        self.val = val
        self.neighbors = []

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        """
        Construct a graph
        For each node:
            if visited, skip
            else:
                components += 1
                add all its kids to visited
        """

        nodes = [Node(i) for i in range(n)]

        for a, b in edges:
            nodes[a].neighbors.append(nodes[b])
            nodes[b].neighbors.append(nodes[a])

        visited = set()
        num_components = 0

        def dfs(node):
            # mark the current node and all its neighbors visited
            if node.val in visited:
                return
            visited.add(node.val)

            for n in node.neighbors:
                dfs(n)
            

        for node in nodes:
            if node.val in visited:
                # print(f"{node.val} visited, skipping")
                continue
            else:
                # print(f"Node {node.val}, new component!")
                num_components += 1
                dfs(node)

        return num_components
            