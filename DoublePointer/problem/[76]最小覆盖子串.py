# 给你一个字符串 s 、一个字符串 t 。返回 s 中涵盖 t 所有字符的最小子串。如果 s 中不存在涵盖 t 所有字符的子串，则返回空字符串 "" 。 
# 
#  
# 
#  注意： 
# 
#  
#  对于 t 中重复字符，我们寻找的子字符串中该字符数量必须不少于 t 中该字符数量。 
#  如果 s 中存在这样的子串，我们保证它是唯一的答案。 
#  
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：s = "ADOBECODEBANC", t = "ABC"
# 输出："BANC"
#  
# 
#  示例 2： 
# 
#  
# 输入：s = "a", t = "a"
# 输出："a"
#  
# 
#  示例 3: 
# 
#  
# 输入: s = "a", t = "aa"
# 输出: ""
# 解释: t 中两个字符 'a' 均应包含在 s 的子串中，
# 因此没有符合条件的子字符串，返回空字符串。 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= s.length, t.length <= 10⁵ 
#  s 和 t 由英文字母组成 
#  
# 
#  
# 进阶：你能设计一个在 o(n) 时间内解决此问题的算法吗？ Related Topics 哈希表 字符串 滑动窗口 👍 1539 👎 0

from collections import defaultdict


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:

    def minWindow(self, s, t):
        '''
        滑动窗口
        '''
        need = defaultdict(int)

        for c in t:
            need[c] += 1

        res = (0, len(s))
        i, j, cnt = 0, 0, len(t)
        while j < len(s):
            if need[s[j]] > 0:
                cnt -= 1
            need[s[j]] -= 1

            if cnt == 0:  # 步骤一：滑动窗口包含了所有T元素
                while True:  # 步骤二：增加i，排除多余元素
                    if need[s[i]] == 0:
                        break
                    need[s[i]] += 1
                    i += 1
                if j - i < res[1] - res[0]:
                    res = (i, j)

                need[s[i]] += 1  # 步骤三：i增加一个位置，寻找新的满足条件滑动窗口\
                cnt += 1
                i += 1
            j += 1
        return '' if res[1] == len(s) else s[res[0]:res[1] + 1]  # 如果res始终没被更新过，代表无满足条件的结果


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == "__main__":
    S = Solution()
    s = "ADOBECODEBANC"
    t = "ABC"

    print(S.minWindow(s, t))
