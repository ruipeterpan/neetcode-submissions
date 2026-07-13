# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        ptr1 = head  # slow
        ptr2 = head  # fast

        while ptr2 and ptr2.next and ptr2.next.next:
            ptr2 = ptr2.next.next
            ptr1 = ptr1.next
            
            if ptr1 == ptr2:
                return True

        # ptr2 has no next, no cycles
        return False