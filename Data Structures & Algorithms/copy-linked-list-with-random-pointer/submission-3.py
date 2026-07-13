"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        old_to_new = {}
        curr = head

        while curr:
            cpy = Node(x=curr.val)
            old_to_new[curr] = cpy
            curr = curr.next

        curr = head
        while curr:
            cpy = old_to_new[curr]
            cpy.next = old_to_new[curr.next] if curr.next else None
            cpy.random = old_to_new[curr.random] if curr.random else None
            curr = curr.next
        
        return old_to_new[head] if head else None


