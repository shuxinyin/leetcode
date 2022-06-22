class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        # Time: O(N), Space: O(1)
        1.哈希表 dic 统计： 指针 j 遍历字符 s ，哈希表统计字符 s[j]最后一次出现的索引 。
        2.更新左指针 i： 根据上轮左指针 i和 dic[s[j]] ，每轮更新左边界i ，
        保证区间 [i + 1, j][i+1,j] 内无重复字符且最大。i = max(dic[s[j]], i)
        3.更新结果 res ： 取上轮 res 和本轮双指针区间 [i + 1,j]的宽度（即j -i）中的最大值。res = max(res, j - i)
        '''
        dic, res, i = dict(), 0, -1
        for j in range(len(s)):
            if s[j] in dic:
                i = max(dic[s[j]], i)
            dic[s[j]] = j
            res = max(res, j-i)
        return res

if __name__ == "__main__":
    s = " "
    S =Solution()
    print(S.lengthOfLongestSubstring(s))