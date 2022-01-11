# 给定一个非空字符串 s，最多删除一个字符。判断是否能成为回文字符串。 
# 
#  
# 
#  示例 1: 
# 
#  
# 输入: s = "aba"
# 输出: true
#  ;
# 
#  示例 2: 
# 
#  
# 输入: s = "abca"
# 输出: true
# 解释: 你可以删除c字符。
#  
# 
#  示例 3: 
# 
#  
# 输入: s = "abc"
# 输出: false 
# 
#  
# 
#  提示: 
# 
#  
#  1 <= s.length <= 10⁵ 
#  s 由小写英文字母组成 
#  
#  Related Topics 贪心 双指针 字符串 👍 439 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def validPalindrome(self, s: str) -> bool:
        '''
        双指针：头尾指针l,r向中间滑动
            当碰到s[l]!=s[r]时，产生两种情况，移动左指针或移动右指针（即删除左字母或右字母）
            所以会产生两个子串s[l+1:r+1]与s[l:r]，判断两个子串是否为回文子串
        Time:O(N)
        Space:O(N)
        由于判断是否回文使用了 [::-1] 翻转形成了新字符串，所以空间复杂度是O(N)。
        如果不通过翻转的方式来判断，空间复杂度可以降到O(1)
        '''
        isPalindrome = lambda s: s == s[::-1]
        l, r = 0, len(s) - 1

        while l < r:
            if s[l] != s[r]:
                return isPalindrome(s[l+1:r+1]) or isPalindrome(s[l:r])
            else:
                l += 1
                r -= 1
        return True




# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    S = Solution()
    s = "cuucu"
    s2 = "ebcbbececabbacecbbcbe"
    print(S.validPalindrome(s))
