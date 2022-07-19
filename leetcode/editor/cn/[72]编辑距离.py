# 给你两个单词 word1 和 word2， 请返回将 word1 转换成 word2 所使用的最少操作数 。 
# 
#  你可以对一个单词进行如下三种操作： 
# 
#  
#  插入一个字符 
#  删除一个字符 
#  替换一个字符 
#  
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：word1 = "horse", word2 = "ros"
# 输出：3
# 解释：
# horse -> rorse (将 'h' 替换为 'r')
# rorse -> rose (删除 'r')
# rose -> ros (删除 'e')
#  
# 
#  示例 2： 
# 
#  
# 输入：word1 = "intention", word2 = "execution"
# 输出：5
# 解释：
# intention -> inention (删除 't')
# inention -> enention (将 'i' 替换为 'e')
# enention -> exention (将 'n' 替换为 'x')
# exention -> exection (将 'n' 替换为 'c')
# exection -> execution (插入 'u')
#  
# 
#  
# 
#  提示： 
# 
#  
#  0 <= word1.length, word2.length <= 500 
#  word1 和 word2 由小写英文字母组成 
#  
#  Related Topics 字符串 动态规划 👍 2485 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        '''DP
        状态： dp[i][j]表示字符串s1[:i] 转换成s2[:j] 需要的最小步数
        转移： if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1]
              else:
                # dp[i-1][j-1] 表示替换操作，dp[i-1][j] 表示删除操作，dp[i][j-1] 表示插入操作
                dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1
        初始化： dp = [[0 for _ in range(n+1)] for j in range(m+1)]
        返回： dp[-1][-1]
        '''
        n1, n2 = len(word1), len(word2)
        dp = [[0] * (n2 + 1) for _ in range(n1 + 1)]

        # 第一行，是s1为空变成s2最少步数，就是插入操作
        for i in range(1, n2 + 1):
            dp[0][i] = dp[0][i - 1] + 1

        # 第一列，是s2为空变成s1最少步数，就是删除操作
        for i in range(1, n2 + 1):
            dp[i][0] = dp[i-1][0] + 1

        for i in range(1, n1+1):
            for j in range(1, n2+1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    # dp[i-1][j-1] 表示替换操作，dp[i-1][j] 表示删除操作，dp[i][j-1] 表示插入操作
                    dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1
        return dp[-1][-1]
# leetcode submit region end(Prohibit modification and deletion)
