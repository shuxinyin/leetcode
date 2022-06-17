class Solution:
    def reverseWords(self, s: str) -> str:
        # Time: O(N), Space: O(N)
        # 双指针 都从右往左
        s = s.strip()
        i = j = len(s) - 1
        res = []
        while i >= 0:
            while i >= 0 and s[i] != ' ':
                i -= 1
            res.append(s[i + 1:j + 1])
            while s[i] == ' ':
                i -= 1
            j = i
        return ' '.join(res)

    def reverseWords_pythonic(self, s: str) -> str:
        s = s.strip()  # 删除首尾空格
        strs = s.split()  # 分割字符串
        strs.reverse()  # 翻转单词列表
        return ' '.join(strs)  # 拼接为字符串并返回



