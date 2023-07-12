# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    reversed_ = ListNode()
    ans_ = ListNode()
    ans_for1_ = ListNode()
    num = 0
    index = 1

    def get_num(self, node: Optional[ListNode], no: int):
        no += 1
        if node.next is not None:
            return self.get_num(node.next, no)
        else:
            return no

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if n == 1:
            num = 0
            self.num = self.get_num(head, num)
            print("num", num)
            idx = 0
            make_for_1(idx)

        self.make_list(head, n)
        print("self.reversed?", self.reversed_)
        # print("ans1", self.ans_)
        self.make_ans(self.reversed_)
        # print("ans2", self.ans_)
        return self.ans_

    def make_for_1(self, node, idx):
        idx += 1
        if idx == self.num - 1:
            return
        self.ans_for1_ = ListNode(node.val)

    def make_list(self, node: Optional[ListNode], remove_no: int):
        if node.next is None and remove_no == 1:
            # self.reversed_ = ListNode()
            return
        if node.next is not None:
            prev = self.make_list(node.next, remove_no)
            self.index += 1
            print(
                "self.index == remove_no:", self.index, remove_no, prev, self.reversed_
            )
            if self.index == remove_no:
                return prev
            if prev is None:
                return
            prev.next = ListNode(node.val, None)
            return prev.next
        else:
            print("koko?")
            self.reversed_ = node
            return node

    def make_ans(self, node: Optional[ListNode]):
        if node.next is not None:
            prev = self.make_ans(node.next)
            prev.next = ListNode(node.val, None)
            return prev.next
        else:
            self.ans_ = node
            return node

    # def delete_last(self, node):
    #     if node.next is None:
    #         return
    #     else:
    #         delete_last
