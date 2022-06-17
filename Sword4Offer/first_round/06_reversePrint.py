# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    '''
    从头到尾打印，可利用栈，后进先出
    '''

    def reversePrint(self, head: ListNode) -> List[int]:
        stack = []
        while head:
            stack.append(head.val)
            head = head.next
        return stack[::-1]


if __name__ == '__main__':
    # 输入：head = [1, 3, 2]
    # 输出：[2, 3, 1]
    print()
