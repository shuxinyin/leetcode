# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        # Time: O(N), Space: O(1)
        # double pointer
        # former 先移动K步，则latter与former间隔K步
        former, latter = head, head
        for _ in range(k):
            if not former:
                return
            former = former.next
        while former:
            former, latter = former.next, latter.next
        return latter
