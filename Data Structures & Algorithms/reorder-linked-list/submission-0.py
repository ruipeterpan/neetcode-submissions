# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        numnodes = 0
        curr = head
        references = []
        while curr:
            references.append(curr)
            curr = curr.next
            numnodes += 1
        
        newhead = references[0]
        prev = newhead
        for i in range(1, numnodes):
            if i % 2 == 0:
                newnode = references[i // 2]
            else:
                newnode = references[numnodes - (i // 2) - 1]
            prev.next = newnode
            prev = newnode
        
        prev.next = None

        # return newhead