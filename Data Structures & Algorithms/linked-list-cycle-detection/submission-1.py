# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False
        hare = head
        turtle = head.next.next
        while turtle and turtle.next:
            if hare.val == turtle.val:
                return True
            hare = hare.next
            turtle = turtle.next.next

        return False