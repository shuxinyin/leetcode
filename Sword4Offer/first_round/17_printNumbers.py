class Solution:
    def printNumbers(self, n: int) -> [int]:
        res = []
        for i in range(1, 10 ** n):
            res.append(i)
        return res


class Solution2:
    def printNumbers(self, n: int) -> [int]:
        # 考虑大数问题
        res = []

        def dfs(x):  # 该递归定义：定x位上的数字
            if x == n:  # 前面n位的数都确定完毕
                num = ''.join(nums)
                while num.startswith('0'):  # 去除首位0
                    num = num[1:]

                if num:
                    res.append(int(num))
                return

            for i in range(0, 10):
                nums[x] = str(i)  # 将x位确定为i
                dfs(x + 1)  # 确定x+1位的数

        nums = ['0'] * n  # 初始化n位的数字
        dfs(0)
        return res


if __name__ == '__main__':
    S =Solution2()

    print(S.printNumbers(0))
