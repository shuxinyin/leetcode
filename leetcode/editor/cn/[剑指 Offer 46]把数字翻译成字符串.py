# 给定一个数字，我们按照如下规则把它翻译为字符串：0 翻译成 “a” ，1 翻译成 “b”，……，11 翻译成 “l”，……，25 翻译成 “z”。
# 一个数字可能有多个翻译。请编程实现一个函数，用来计算一个数字有多少种不同的翻译方法。
# 
#  
# 
#  示例 1: 
# 
#  输入: 12258
# 输出: 5
# 解释: 12258有5种不同的翻译，分别是"bccfi", "bwfi", "bczi", "mcfi"和"mzi" 
# 
#  
# 
#  提示： 
# 
#  
#  0 <= num < 2³¹ 
#  
#  Related Topics 字符串 动态规划 👍 449 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def translateNum(self, num: int) -> int:
        '''
        dp[i]: 以字母num[i]结尾的翻译方法数
        转移： if nums[i-1]==1, dp[i]= dp[i-1] + dp[i-2]， 最后两个字母单独翻译 + 一起翻译
            elif nums[i-1] == 2 and 0<=nums[i]<6, dp[i]= dp[i-1] + dp[i-2]， 最后两个字母单独翻译 + 一起翻译
            else dp[i] = dp[i-1]
            综合起来： dp[i] = dp[i-1] + dp[i-2], if '10'<=num[i-1:i+1]<='25'
                    dp[i] = dp[i-1]
        初始状态： dp[0]=dp[1]=1,即 “无数字” 和 “第 1位数字” 的翻译方法数量为 1
        '''
        s = str(num)
        n = len(s)

        dp = [0] * (n + 1)
        dp[0] = dp[1] = 1
        for i in range(2, n + 1):
            if '10' <= s[i - 2:i] <= '25':
                dp[i] = dp[i - 1] + dp[i - 2]
            else:
                dp[i] = dp[i - 1]
        return dp[-1]

    def translateNum2(self, num: int) -> int:
        ''' 滚动变量做法
        1. dp 表示当前位置结尾字符上的最大种翻译方法
        2.  若是x_i与x_i-1组成的数字可被翻译 dp[i] = dp[i-1]+dp[i-2], 反之，dp[i]=dp[i-1]
        初始状态 dp[0]=nums[0]
        '''
        s = str(num)
        a, b = 1, 1
        for i in range(2, len(s) + 1):
            tmp = s[i - 2:i]
            c = a + b if "10" <= tmp <= "25" else a

            b = a
            a = c
        return a


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    S = Solution()

    num = 25
    print(S.translateNum(num))
