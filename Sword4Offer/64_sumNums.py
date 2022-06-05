class Solution:
    def sumNums(self, n: int) -> int:
        # python的 and 操作如果最后结果为真，返回最后一个表达式的值，or 操作如果结果为真，返回第一个结果为真的表达式的值
        # Time = O(N), 计算 n + (n-1) + ... + 2 + 1  n个递归函数
        # Space = O(N), 递归深度为n,需要使用O(n)的额外函数
        return n and (n + self.sumNums(n - 1))

    def sumNums_recur(self, n: int) -> int:
        if n == 1:
            return 1
        n += self.sumNums(n - 1)
