# 给定一个非负整数 c ，你要判断是否存在两个整数 a 和 b，使得 a² + b² = c 。 
# 
#  
# 
#  示例 1： 
# 
#  输入：c = 5
# 输出：true
# 解释：1 * 1 + 2 * 2 = 5
#  
# 
#  示例 2： 
# 
#  输入：c = 3
# 输出：false
#  
# 
#  示例 3： 
# 
#  输入：c = 4
# 输出：true
#  
# 
#  示例 4： 
# 
#  输入：c = 2
# 输出：true
#  
# 
#  示例 5： 
# 
#  输入：c = 1
# 输出：true 
# 
#  
# 
#  提示： 
# 
#  
#  0 <= c <= 2³¹ - 1 
#  
#  Related Topics 数学 双指针 二分查找 👍 326 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        # 时间复杂度为 O(sqrt(c)) solution 633 is valuable
        l, r = 0, int(c ** 0.5)
        while l <= r:
            if l ** 2 + r ** 2 < c:
                l += 1
            elif l ** 2 + r ** 2 > c:
                r -= 1
            else:
                return True
        return False


# leetcode submit region end(Prohibit modification and deletion)

if __name__ == "__main__":
    S = Solution()
    c = 2
    print(S.judgeSquareSum(c))
