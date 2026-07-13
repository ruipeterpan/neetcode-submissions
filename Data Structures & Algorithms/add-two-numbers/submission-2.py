# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        result = self.addTwoNumbersHelper(l1, l2, carryover=False)
        if not result:
            result = ListNode()
        
        return result

    def addTwoNumbersHelper(self, l1: Optional[ListNode], l2: Optional[ListNode], carryover=False):
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0

        new_val = val1 + val2 + int(carryover)
        if new_val >= 10:
            new_val -= 10
            carryover = True
        else:
            carryover = False
        if new_val == 0 and not carryover:
            return None
        new_node = ListNode(val=new_val)
        new_l1 = l1.next if l1 else None
        new_l2 = l2.next if l2 else None
        new_node.next = self.addTwoNumbersHelper(new_l1, new_l2, carryover)
        return new_node


