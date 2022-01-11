# 给你一个字符串 s 和一个字符串数组 dictionary ，找出并返回 dictionary 中最长的字符串，该字符串可以通过删除 s 中的某些字符得到。
#  
# 
#  如果答案不止一个，返回长度最长且字母序最小的字符串。如果答案不存在，则返回空字符串。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：s = "abpcplea", dictionary = ["ale","apple","monkey","plea"]
# 输出："apple"
#  
# 
#  示例 2： 
# 
#  
# 输入：s = "abpcplea", dictionary = ["a","b","c"]
# 输出："a"
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= s.length <= 1000 
#  1 <= dictionary.length <= 1000 
#  1 <= dictionary[i].length <= 1000 
#  s 和 dictionary[i] 仅由小写英文字母组成 
#  
#  Related Topics 数组 双指针 字符串 排序 👍 283 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findLongestWord(self, s, dictionary):
        '''
        归并两个有序数组的变形题, 思路基本一致。
        '''
        dictionary = sorted(dictionary, key=lambda x: (-len(x), x))

        for word in dictionary:
            p1, p2 = len(word) - 1, len(s) - 1
            while p1 >= 0 and p2 >= 0:
                if word[p1] == s[p2]:
                    p1 -= 1
                    p2 -= 1
                else:
                    p2 -= 1
            if p1 == -1:
                return word
        return ''


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == '__main__':
    dictionary = ["ale", "apple", "monk", "plea"]
    dictionary = ["abe", "abc"]
    dictionary = sorted(dictionary, key=lambda x: (-len(x), x))
    print(dictionary)

    s = "abpcplea"
    S = Solution()
    print(S.findLongestWord(s, dictionary))
    print('abc'<'abe')
