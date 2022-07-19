# 给你一个字符串 s，找到 s 中最长的回文子串。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：s = "babad"
# 输出："bab"
# 解释："aba" 同样是符合题意的答案。
#  
# 
#  示例 2： 
# 
#  
# 输入：s = "cbbd"
# 输出："bb"
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= s.length <= 1000 
#  s 仅由数字和英文字母组成 
#  
#  Related Topics 字符串 动态规划 👍 5462 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def expandAroundCenter(self, s, left, right):
        ''' 进行扩展
        '''
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return left + 1, right - 1

    def longestPalindrome(self, s: str) -> str:
        ''' 中心扩展算法：枚举所有的「回文中心」并尝试「扩展」，直到无法扩展为止
            回文子串存在两种情况： 1. cbabc(奇数), 2. cbbc（偶数）
            Time: O(n^2)
            Space: O(1)
        '''
        start, end = 0, 0
        for i in range(len(s)):
            left1, right1 = self.expandAroundCenter(s, i, i)  # 1. cbabc(奇数)
            left2, right2 = self.expandAroundCenter(s, i, i + 1)  # 2. cbbc（偶数）

            if right1 - left1 > end - start:
                start, end = left1, right1
            if right2 - left2 > end - start:
                start, end = left2, right2
        return s[start: end + 1]

# leetcode submit region end(Prohibit modification and deletion)

class Solution_manacher:
    def longestPalindrome(self, s: str) -> str:
        '''
        Time: O(N)
        Space: O(N)
        '''
        pass

