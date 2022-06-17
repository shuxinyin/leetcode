class Solution:
    def findNumberIn2DArray(self, matrix, target: int) -> bool:
        # Time: O(Nlog(N)), Space: O(1)

        if not matrix:
            return False

        row = len(matrix)
        col = len(matrix[0])

        i, j = 0, col - 1
        for i in range(row):
            while 0 <= i < row and 0 <= j < col:
                if matrix[i][j] == target:
                    return True
                elif matrix[i][j] < target:
                    i += 1
                else:
                    j -= 1

        return False



if __name__ == '__main__':
    mat = [[1, 4, 7, 11, 15],
           [2, 5, 8, 12, 19],
           [3, 6, 9, 16, 22],
           [10, 13, 14, 17, 24],
           [18, 21, 23, 26, 30]]

    S = Solution()
    print(S.findNumberIn2DArray(mat, 5))
