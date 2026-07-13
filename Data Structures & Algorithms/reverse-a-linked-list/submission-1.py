# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None        # The already-reversed part of the list; starts empty
        curr = head        # The node we are currently processing in the original list

        while curr:
            next = curr.next  # the part of the list that hasn't been reversed
            
            curr.next = prev
            prev = curr

            curr = next
        
        return prev