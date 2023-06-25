# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return
        top = ListNode()
        prev = None
        while head.next:
            current = ListNode(val=head.val, next=prev)
            prev = current
            head = head.next
        current = ListNode(val=head.val, next=prev)
        return current
