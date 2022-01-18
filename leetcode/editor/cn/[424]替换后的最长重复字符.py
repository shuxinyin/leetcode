# 给你一个仅由大写英文字母组成的字符串，
# 你可以将任意位置上的字符替换成另外的字符，总共可最多替换 k 次。
# 在执行上述操作后，找到包含重复字母的最长子串的长度。
#  
# 
#  注意：字符串长度 和 k 不会超过 10⁴。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：s = "ABAB", k = 2
# 输出：4
# 解释：用两个'A'替换为两个'B',反之亦然。
#  
# 
#  示例 2： 
# 
#  
# 输入：s = "AABABBA", k = 1
# 输出：4
# 解释：
# 将中间的一个'A'替换为'B',字符串变为 "AABBBBA"。
# 子串 "BBBB" 有最长重复字母, 答案为 4。
#  
#  Related Topics 哈希表 字符串 滑动窗口 👍 541 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        from collections import defaultdict
        dic = defaultdict(int)
        n = len(s)
        maxn, l, r = 0, 0, 0

        while r < n:
            dic[s[r]] += 1
            maxn = max(maxn, dic[s[r]])
            if r - l + 1 - maxn > k:  # 子字符串长度-最大重复字符数>k
                dic[s[l]] -= 1
                l += 1
            r += 1  # 这里加了1，所以return 不+1
        return r - l


# leetcode submit region end(Prohibit modification and deletion)

if __name__ == '__main__':
    s = "ABAB"
    s = "AABABBA"
    S = Solution()
    print(S.characterReplacement(s, 1))
