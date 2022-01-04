# 假设有一个很长的花坛，一部分地块种植了花，另一部分却没有。可是，花不能种植在相邻的地块上，它们会争夺水源，两者都会死去。 
# 
#  给你一个整数数组 flowerbed 表示花坛，由若干 0 和 1 组成，其中 0 表示没种植花，1 表示种植了花。另有一个数 n ，能否在不打破种植规则
# 的情况下种入 n 朵花？能则返回 true ，不能则返回 false。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：flowerbed = [1,0,0,0,1], n = 1
# 输出：true
#  
# 
#  示例 2： 
# 
#  
# 输入：flowerbed = [1,0,0,0,1], n = 2
# 输出：false
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= flowerbed.length <= 2 * 10⁴ 
#  flowerbed[i] 为 0 或 1 
#  flowerbed 中不存在相邻的两朵花 
#  0 <= n <= flowerbed.length 
#  
#  Related Topics 贪心 数组 👍 413 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def canPlaceFlowers(self, flowerbed, n) -> bool:
        '''
        两格连跳方法：因为如果遇到1,那么下一格子一定是0，这是毋庸置疑的（规则限定：花儿不能相邻）
        所以如果遇到当前位置i为最后一个格子，或者i的下个格子不是1，果断种花填充。
        '''
        i = 0
        while i < len(flowerbed):
            if flowerbed[i] == 0:
                if (i == len(flowerbed) - 1) or (flowerbed[i + 1] == 0):
                    n -= 1
                else:
                    i += 1
            i += 2
        return n <= 0


# leetcode submit region end(Prohibit modification and deletion)

if __name__ == "__main__":
    S = Solution()
    result = S.canPlaceFlowers([1, 0, 0, 0, 1], 1)
    print(result)
