# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # method1: double pointer
        # exist three pointer exactly: pre, cur, cur.next
        pre, cur = None, head

        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        return pre

    def reverseList2(self, head: ListNode) -> ListNode:
        # method2: Recurrence Method
        def recur(cur, pre):
            if not cur:
                return pre

            res = recur(cur.next, cur)
            cur.next = pre
            return res

        return recur(head, None)
