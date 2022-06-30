# 请从字符串中找出一个最长的不包含重复字符的子字符串，计算该最长子字符串的长度。 
# 
#  
# 
#  示例 1: 
# 
#  输入: "abcabcbb"
# 输出: 3 
# 解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
#  
# 
#  示例 2: 
# 
#  输入: "bbbbb"
# 输出: 1
# 解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
#  
# 
#  示例 3: 
# 
#  输入: "pwwkew"
# 输出: 3
# 解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
#      请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
#  
# 
#  
# 
#  提示： 
# 
#  
#  s.length <= 40000 
#  
# 
#  注意：本题与主站 3 题相同：https://leetcode-cn.com/problems/longest-substring-without-
# repeating-characters/ 
#  Related Topics 哈希表 字符串 滑动窗口 👍 450 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        # Time: O(N), Space: O(1)
        1.哈希表 dic 统计： 指针 j 遍历字符 s ，哈希表统计字符 s[j]最后一次出现的索引 。
        2.当s[j] in dic: 更新左指针i, 根据上轮左指针 i和 dic[s[j]] ，每轮更新左边界i ，
        保证区间 [i + 1, j] 内无重复字符且最大。i = max(dic[s[j]], i)
        3.更新结果 res ： 取上轮 res 和本轮双指针区间 [i + 1,j]的宽度（即j -i）中的最大值。res = max(res, j - i)
        '''
        dic, res, i = dict(), 0, -1
        for j in range(len(s)):
            if s[j] in dic:
                i = max(dic[s[j]], i)
            dic[s[j]] = j  # 哈希表更新最后一次索引
            res = max(res, j-i)
        return res
# leetcode submit region end(Prohibit modification and deletion)
