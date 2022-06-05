class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = list()
        for i in range(numRows):
            row = list()
            for j in range(i + 1):
                if j == 0 or j == i:
                    row.append(1)
                else:
                    row.append(res[i - 1][j - 1] + res[i - 1][j])
            res.append(row)
        return res