# 给定一个非负索引 rowIndex，返回「杨辉三角」的第 rowIndex 行。 
# 
#  在「杨辉三角」中，每个数是它左上方和右上方的数的和。 
# 
#  
# 
#  
# 
#  示例 1: 
# 
#  
# 输入: rowIndex = 3
# 输出: [1,3,3,1]
#  
# 
#  示例 2: 
# 
#  
# 输入: rowIndex = 0
# 输出: [1]
#  
# 
#  示例 3: 
# 
#  
# 输入: rowIndex = 1
# 输出: [1,1]
#  
# 
#  
# 
#  提示: 
# 
#  
#  0 <= rowIndex <= 33 
#  
# 
#  
# 
#  进阶： 
# 
#  你可以优化你的算法到 O(rowIndex) 空间复杂度吗？ 
#  Related Topics 数组 动态规划 👍 408 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        '''
        状态： dp[i] 表示
        '''
        pre = []
        for i in range(rowIndex + 1):
            row = []
            for j in range(i + 1):
                if j == 0 or j == i:
                    row.append(1)
                else:
                    row.append(pre[j - 1] + pre[j])
            pre = row
        return pre

# leetcode submit region end(Prohibit modification and deletion)
