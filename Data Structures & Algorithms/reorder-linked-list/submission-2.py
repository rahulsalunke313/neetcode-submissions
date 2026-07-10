# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return
        p1 = head
        p2 = head.next.next
        while p2 and p2.next:
            p1 = p1.next
            p2 = p2.next.next
        l2 = p1.next
        p1.next = None
        print(p1.val, l2.val)
        # l2 = reverse(l2)
        prev, cur = None, l2
        while cur:
            cur.next, cur, prev = prev, cur.next, cur
        l2 = prev

        l1 = head

        current = l1
        while current is not None:
            print(current.val, end=" -> ")
            current = current.next  # Move to the next node
        print("None")


        current = l2
        while current is not None:
            print(current.val, end=" -> ")
            current = current.next  # Move to the next node
        print("None")
        

        res = p = ListNode(None)
        while l1 and l2:
            print(p.val,l1.val,l2.val)
            p.next = l1
            l1 = l1.next
            p.next.next = l2
            l2 = l2.next
            p = p.next.next

        if l1:
            p.next = l1
        if l2:
            p.next = l2
        






