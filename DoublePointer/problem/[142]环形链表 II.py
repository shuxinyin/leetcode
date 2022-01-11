# 给定一个链表，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。 
# 
#  如果链表中有某个节点，可以通过连续跟踪 next 指针再次到达，则链表中存在环。 为了表示给定链表中的环，评测系统内部使用整数 pos 来表示链表尾连接到
# 链表中的位置（索引从 0 开始）。如果 pos 是 -1，则在该链表中没有环。注意：pos 不作为参数进行传递，仅仅是为了标识链表的实际情况。 
# 
#  不允许修改 链表。 
# 
#  
#  
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  
# 输入：head = [3,2,0,-4], pos = 1
# 输出：返回索引为 1 的链表节点
# 解释：链表中有一个环，其尾部连接到第二个节点。
#  
# 
#  示例 2： 
# 
#  
# 
#  
# 输入：head = [1,2], pos = 0
# 输出：返回索引为 0 的链表节点
# 解释：链表中有一个环，其尾部连接到第一个节点。
#  
# 
#  示例 3： 
# 
#  
# 
#  
# 输入：head = [1], pos = -1
# 输出：返回 null
# 解释：链表中没有环。
#  
# 
#  
# 
#  提示： 
# 
#  
#  链表中节点的数目范围在范围 [0, 10⁴] 内 
#  -10⁵ <= Node.val <= 10⁵ 
#  pos 的值为 -1 或者链表中的一个有效索引 
#  
# 
#  
# 
#  进阶：你是否可以使用 O(1) 空间解决此题？ 
#  Related Topics 哈希表 链表 双指针 👍 1307 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        '''
        第一次相遇时：
        slow指针走过的节点数为: x + y,fast指针走过的节点数： x + y + n (y + z)，n为圈数，（y+z）为 一圈内节点的个数
        因为fast指针是一步走两个节点，slow指针一步走一个节点， 所以 fast指针走过的节点数 = slow指针走过的节点数 * 2
        (x + y) * 2 = x + y + n (y + z)
        消掉（x+y）: x + y = n (y + z)
        因为我们要找环形的入口，那么要求的是x，因为x表示 头结点到 环形入口节点的的距离。
        所以我们要求x ，将x单独放在左面：x = n (y + z) - y
        y融合进去，整理公式之后：x = (n - 1) (y + z) + z
        注意这里n一定是大于等于1的，因为 fast指针至少要多走一圈才能相遇slow指针
        1.当 n为1的时候，公式就化解为 x = z
            这就意味着，从头结点出发一个指针，从相遇节点 也出发一个指针，这两个指针每次只走一个节点，
            那么当这两个指针相遇的时候就是 环形入口的节点
            也就是在相遇节点处，定义一个指针index1，在头结点处定一个指针index2。
            让index1和index2同时移动，每次移动一个节点， 那么他们相遇的地方就是 环形入口的节点。
        2.那么n如果大于1是什么情况呢，就是fast指针在环形转n圈之后才遇到 slow指针。
            其实这种情况和n为1的时候 效果是一样的，一样可以通过这个方法找到 环形的入口节点，
            只不过，index1 指针在环里 多转了(n-1)圈，然后再遇到index2，相遇点依然是环形的入口节点。
        '''
        fast, slow = head, head
        while fast and fast.next:
            fast, slow = fast.next.next, slow.next

            if fast == slow:
                fast = head
                while fast != slow:
                    fast, slow = fast.next, slow.next
                return fast
        return None


class Solution2:
    def detectCycle(self, head):
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            # 如果相遇
            if slow == fast:
                p = head
                q = slow
                while p != q:
                    p = p.next
                    q = q.next
                # 你也可以return q
                return p

        return None
# leetcode submit region end(Prohibit modification and deletion)
