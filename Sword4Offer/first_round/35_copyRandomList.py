# source code https://leetcode-cn.com/problems/fu-za-lian-biao-de-fu-zhi-lcof/solution/jian-zhi-offer-35-fu-za-lian-biao-de-fu-zhi-ha-xi-/
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        # hash
        # Time: O(N), Space: O(N)
        if not head:
            return
        dic = {}

        # 3. 复制各节点，并建立 “原节点 -> 新节点” 的 Map 映射
        cur = head
        while cur:
            dic[cur] = Node(cur.val)
            cur = cur.next

        # 4. 构建新节点的 next 和 random 指向
        cur = head
        while cur:
            dic[cur].next = dic.get(cur.next)  # new_node.next = source_node.next
            dic[cur].random = dic.get(cur.random)  # new_node.random = source_node.random
            cur = cur.next

        # 5. 返回新链表的头节点
        return dic[head]


class Solution2:
    def copyRandomList(self, head: 'Node') -> 'Node':
        # 拼接 + 拆分
        # Time: O(N), Space: O(1)
        if not head:
            return
        cur = head

        # 1.复制各节点，并构建拼接链表
        while cur:
            tmp = Node(cur.val)
            tmp.next = cur.next
            cur.next = tmp
            cur = tmp.next

        # 2. 构建各新节点的 random 指向
        cur = head
        while cur:
            if cur.random:
                cur.next.random = cur.random.next
            cur = cur.next.next

        # 3. 拆分两链表
        cur = res = head.next
        pre = head
        while cur.next:
            pre.next = pre.next.next
            cur.next = cur.next.next
            pre = pre.next
            cur = cur.next
        pre.next = None  # 单独处理原链表尾节点

        return res  # 返回新链表头节点
