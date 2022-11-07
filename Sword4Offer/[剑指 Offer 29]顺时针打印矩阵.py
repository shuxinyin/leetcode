# 输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字。 
# 
#  
# 
#  示例 1： 
# 
#  输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
# 输出：[1,2,3,6,9,8,7,4,5]
#  
# 
#  示例 2： 
# 
#  输入：matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# 输出：[1,2,3,4,8,12,11,10,9,5,6,7]
#  
# 
#  
# 
#  限制： 
# 
#  
#  0 <= matrix.length <= 100 
#  0 <= matrix[i].length <= 100 
#  
# 
#  注意：本题与主站 54 题相同：https://leetcode-cn.com/problems/spiral-matrix/ 
#  Related Topics 数组 矩阵 模拟 👍 455 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def spiralOrder(self, matrix: [[int]]) -> [int]:
        ''' 从左向右、从上向下、从右向左、从下向上
        设置4个边界，left, right, top, bottom
        '''
        if not matrix:
            return []

        l, r, t, b = 0, len(matrix[0]) - 1, 0, len(matrix) - 1
        res = []
        while True:
            for i in range(l, r + 1):
                res.append(matrix[t][i])  # left to right
            t += 1
            if t > b:
                break

            for i in range(t, b + 1):
                res.append(matrix[i][r])  # top to bottom
            r -= 1
            if l > r:
                break

            for i in range(r, l - 1, -1):
                res.append(matrix[b][i])  # right to left
            b -= 1
            if t > b:
                break

            for i in range(b, t - 1, -1):
                res.append(matrix[i][l])  # bottom to top
            l += 1
            if l > r:
                break
        return res

# leetcode submit region end(Prohibit modification and deletion)
