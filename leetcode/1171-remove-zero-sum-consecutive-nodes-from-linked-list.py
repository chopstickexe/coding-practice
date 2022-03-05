# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy_head = ListNode()  # Required for the case when the original head is removed
        dummy_head.next = head
        head = dummy_head
        
        cs = 0
        sums = {}  # Key: cumulative sum, Value: node where the sum is obtained　last
        while head:
            cs += head.val
            sums[cs] = head
            head = head.next
        
        head = dummy_head
        cs = 0
        while head:
            cs += head.val
            head.next = sums[cs].next
            head = head.next
        
        return dummy_head.next
        