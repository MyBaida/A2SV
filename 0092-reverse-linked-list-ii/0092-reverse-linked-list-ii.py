# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        if not head or head.next == None:
            return head

        dummy = ListNode(0)
        dummy.next = head
        leftPrev = dummy

        for _ in range(left-1):
            leftPrev = leftPrev.next

        curr = leftPrev.next
        prev = None

        for _ in range(right-left+1):
            next = curr.next
            curr.next = prev
            
            prev = curr
            curr = next

        leftPrev.next.next = curr
        leftPrev.next = prev

        return dummy.next