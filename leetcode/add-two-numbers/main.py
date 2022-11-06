# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        last = ListNode()
        ans = last
        amari = 0
        while True:
            ret = self.calc(l1, l2)
            last.val = str((ret + amari) % 10)
            amari = (ret + amari) // 10
            if l1.next is None and l2.next is None and amari == 1:
                last.next = ListNode(val=1)
                break
            if l1.next is None and l2.next is None:
                break
            elif l1.next is not None and l2.next is not None:
                l1 = l1.next
                l2 = l2.next
            elif l1.next is not None:
                l1 = l1.next
                l2 = ListNode()
            elif l2.next is not None:
                l2 = l2.next
                l1 = ListNode()

            last.next = ListNode()
            last = last.next

        return ans

    def calc(self, l1: Optional[ListNode], l2: Optional[ListNode]):
        if l1 != None and l2 != None:
            return l1.val + l2.val
        elif l1 != None:
            return l1.val
        else:
            return l2.val
