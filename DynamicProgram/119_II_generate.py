class Solution:
    def getRow(self, rowIndex: int) -> [int]:
        pre = list()
        for i in range(rowIndex + 1):
            cur = list()
            for j in range(i + 1):
                if j == 0 or j == i:
                    cur.append(1)
                else:
                    cur.append(pre[j - 1] + pre[j])
            pre = cur
        return pre

    def getRow2(self, rowIndex: int) -> [int]:
        # 倒着计算当前行，这样计算到第 ii 项时，第 i-1i−1 项仍然是上一行的值。
        res = [0] * (rowIndex + 1)
        res[0] = 1
        for i in range(rowIndex + 1):
            for j in range(i, 0, -1):
                print(res)
                res[j] += res[j - 1]
        return res


if __name__ == '__main__':
    S = Solution()
    print(S.getRow2(3))
