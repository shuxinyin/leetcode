# 一条包含字母 A-Z 的消息通过以下映射进行了 编码 ： 
# 
#  
# 'A' -> "1"
# 'B' -> "2"
# ...
# 'Z' -> "26" 
# 
#  要 解码 已编码的消息，所有数字必须基于上述映射的方法，反向映射回字母（可能有多种方法）。例如，"11106" 可以映射为： 
# 
#  
#  "AAJF" ，将消息分组为 (1 1 10 6) 
#  "KJF" ，将消息分组为 (11 10 6) 
#  
# 
#  注意，消息不能分组为 (1 11 06) ，因为 "06" 不能映射为 "F" ，这是由于 "6" 和 "06" 在映射中并不等价。 
# 
#  给你一个只含数字的 非空 字符串 s ，请计算并返回 解码 方法的 总数 。 
# 
#  题目数据保证答案肯定是一个 32 位 的整数。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：s = "12"
# 输出：2
# 解释：它可以解码为 "AB"（1 2）或者 "L"（12）。
#  
# 
#  示例 2： 
# 
#  
# 输入：s = "226"
# 输出：3
# 解释：它可以解码为 "BZ" (2 26), "VF" (22 6), 或者 "BBF" (2 2 6) 。
#  
# 
#  示例 3： 
# 
#  
# 输入：s = "0"
# 输出：0
# 解释：没有字符映射到以 0 开头的数字。
# 含有 0 的有效映射是 'J' -> "10" 和 'T'-> "20" 。
# 由于没有字符，因此没有有效的方法对此进行解码，因为所有数字都需要映射。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= s.length <= 100 
#  s 只包含数字，并且可能包含前导零。 
#  
#  Related Topics 字符串 动态规划 👍 1199 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def numDecodings(self, s: str) -> int:
        '''
        状态： dp[i] 表示 以 nums[i] 结尾的子序列的等差数据列个数
        转移：
                if s[i] == 0:
                    # 10 or 20 必须绑定在一起翻译， dp[i] = dp[i - 2]
                    if s[i - 1] == '1' or s[i - 1] == '2':
                        dp[i] = dp[i - 2]
                    else
                        return 0
                else
                    if 10<s[i-1:i] <27:  # 可分开逐个或 在一起翻译
                        dp[i] = dp[i-2] + dp[i-1]
                    else:
                        dp[i] = dp[i-1]  # 必须分开，逐个翻译
        初始状态：  dp[0] = dp[-1] = 1, (为了把dp)
        # 由于 dp[i-2]的存在，所以 dp 的长度要 len（s）+1 ，留出 dp[-1] = 1
        返回： dp[n-1]

        '''

        n = len(s)
        dp = [1] * (n + 1)
        dp[0] = dp[-1] = 1

        for i in range(1, n):
            if s[i] == '0':
                # 10 or 20 必须绑定在一起翻译， dp[i] = dp[i - 2]
                if s[i - 1] == '1' or s[i - 1] == '2':
                    dp[i] = dp[i - 2]
                else:
                    return 0
            else:
                if '10' < s[i - 1:i+1] < '27':  # 可分开逐个或 在一起翻译
                    dp[i] = dp[i - 2] + dp[i - 1]
                else:
                    dp[i] = dp[i - 1]  # 必须分开，逐个翻译
        return dp[n-1]

# leetcode submit region end(Prohibit modification and deletion)
