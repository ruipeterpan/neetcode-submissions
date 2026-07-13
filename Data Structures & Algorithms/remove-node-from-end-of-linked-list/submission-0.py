# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # first pass: count num nodes
        num_nodes = 0
        count_ptr = head
        while count_ptr:
            num_nodes += 1
            count_ptr = count_ptr.next
        print(f"num_nodes {num_nodes}")

        # second pass: get to the nth node
        idx_of_tombstone = num_nodes - n
        print(f"idx_of_tombstone {idx_of_tombstone}")  # need to remove this node at index idx_of_tombstone

        if idx_of_tombstone == 0:
            return head.next

        ptr = head
        for i in range(idx_of_tombstone - 1):
            ptr = ptr.next
        ptr.next = ptr.next.next  # remove ptr.next

        return head
