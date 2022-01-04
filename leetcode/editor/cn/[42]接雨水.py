# 给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。 
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  
# 输入：height = [0,1,0,2,1,0,1,3,2,1,2,1]
# 输出：6
# 解释：上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。 
#  
# 
#  示例 2： 
# 
#  
# 输入：height = [4,2,0,3,2,5]
# 输出：9
#  
# 
#  
# 
#  提示： 
# 
#  
#  n == height.length 
#  1 <= n <= 2 * 10⁴ 
#  0 <= height[i] <= 10⁵ 
#  
#  Related Topics 栈 数组 双指针 动态规划 单调栈 👍 2967 👎 0


# leetcode submit region begin(Prohibit modification and deletion)

class Solution:
    '''
    按竖列单个算:（造一个局部凹凸点）：
    左边取一个最大高度max_left, 右边取一个最大高度max_left，单独算每一个竖列位置i能装多少水
    分两种情况：1. max_left <= i <= max_right： 无法接水
            2. i < max_right，max_left ： 接水量 min(max_left, max_right) - h[i]
    '''
    def trap(self, height):
        # 边界条件
        if not height: return 0
        n = len(height)

        left, right = 1, n - 2  # 分别位于输入数组的两端
        max_left, max_right = height[0], height[n - 1]
        res = 0

        while left <= right:
            max_left = max(height[left], max_left)
            max_right = max(height[right], max_right)
            # 下面这两种情况,保证了现在在计算的位置一定是不大于左右的，保证了局部最小
            # 这样就免去了，每个位置都去搜索全局最大（如方法2）
            # 1.保证了 h[left]<=max_left<max_right
            # 2.保证了 h[right]<=max_right<max_left
            if max_left < max_right:
                res += max_left - height[left]
                left += 1
            else:
                res += max_right - height[right]
                right -= 1

        return res

    def trap2(self, height):
        length = len(height)
        res = 0
        for i in range(1, length - 1):
            max_left, max_right = max(height[:i]), max(height[i:])
            min_height = min(max_left, max_right)
            if height[i] < min_height:
                res += min_height - height[i]
        return res

# leetcode submit region end(Prohibit modification and deletion)
