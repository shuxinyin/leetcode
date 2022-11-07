# 输入一个非负整数数组，把数组里所有数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。 
# 
#  
# 
#  示例 1: 
# 
#  输入: [10,2]
# 输出: "102" 
# 
#  示例 2: 
# 
#  输入: [3,30,34,5,9]
# 输出: "3033459" 
# 
#  
# 
#  提示: 
# 
#  
#  0 < nums.length <= 100 
#  
# 
#  说明: 
# 
#  
#  输出结果可能非常大，所以你需要返回一个字符串而不是整数 
#  拼接起来的数字可能会有前导 0，最后结果不需要去掉前导 0 
#  
#  Related Topics 贪心 字符串 排序 👍 488 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minNumber(self, nums: [int]) -> str:
        # if x + y > y + x: 则x > y, keep its order
        # 反之 x + y < y + x: 则x < y, exchange
        # 快速排序
        def quick_sort(l, r):
            if l >= r:
                return
            i, j = l, r
            while i < j:
                while strs[j] + strs[l] >= strs[l] + strs[j] and i < j:
                    j -= 1
                while strs[i] + strs[l] <= strs[l] + strs[i] and i < j:
                    i += 1
                strs[i], strs[j] = strs[j], strs[i]
            strs[i], strs[l] = strs[l], strs[i]
            quick_sort(l, i - 1)
            quick_sort(i + 1, r)

        strs = [str(num) for num in nums]
        quick_sort(0, len(strs) - 1)
        return ''.join(strs)
# leetcode submit region end(Prohibit modification and deletion)
