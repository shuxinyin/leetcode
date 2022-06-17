class Solution:
    def verifyPostorder(self, postorder: List[int]) -> bool:
        # 时间复杂度O(N ^ 2)： 每次调用recur(i, j)减去一个根节点，因此递归占用O(N)；最差情况下（即当树退化为链表）while循环每轮递归都需遍历树所有节点，占用O(N)。
        # 空间复杂度O(N)： 最差情况下（即当树退化为链表），递归深度将达到N
        def recur(i, j):
            if i >= j:
                return True

            p = i
            while postorder[p] < postorder[j]:
                p += 1
            m = p
            while postorder[p] > postorder[j]:
                p += 1
            return p == j and recur(i, m) and recur(m, j - 1)

        return recur(0, len(postorder) - 1)

    def verifyPostorder_stack(self, postorder: List[int]) -> bool:
        # 单调栈  ##
        # 时间复杂度O(N)
        # 空间复杂度O(N)
        stack, root = [], float("+inf")
        for i in range(len(postorder) - 1, -1, -1):
            if postorder[i] > root: return False
            while (stack and postorder[i] < stack[-1]):
                root = stack.pop()
            stack.append(postorder[i])
        return True

    def verifyPostorder_bst(self, postorder: List[int]) -> bool:
        import sys

        def build(postorder: List[int], ma: int, mi: int):
            if not postorder: return
            val = postorder[-1]
            if not mi < val < ma: return
            postorder.pop()  # 根
            build(postorder, ma, val)  # 右
            build(postorder, val, mi)  # 左

        build(postorder, sys.maxsize, -sys.maxsize)
        return not postorder
