# 字典 wordList 中从单词 beginWord 和 endWord 的 转换序列 是一个按下述规格形成的序列 beginWord -> s1 -> 
# s2 -> ... -> sk： 
# 
#  
#  每一对相邻的单词只差一个字母。 
#  对于 1 <= i <= k 时，每个 si 都在 wordList 中。注意， beginWord 不需要在 wordList 中。 
#  sk == endWord 
#  
# 
#  给你两个单词 beginWord 和 endWord 和一个字典 wordList ，返回 从 beginWord 到 endWord 的 最短转换序列 
# 中的 单词数目 。如果不存在这样的转换序列，返回 0 。 
#  
# 
#  示例 1： 
# 
#  
# 输入：beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot",
# "log","cog"]
# 输出：5
# 解释：一个最短转换序列是 "hit" -> "hot" -> "dot" -> "dog" -> "cog", 返回它的长度 5。
#  
# 
#  示例 2： 
# 
#  
# 输入：beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot",
# "log"]
# 输出：0
# 解释：endWord "cog" 不在字典中，所以无法进行转换。 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= beginWord.length <= 10 
#  endWord.length == beginWord.length 
#  1 <= wordList.length <= 5000 
#  wordList[i].length == beginWord.length 
#  beginWord、endWord 和 wordList[i] 由小写英文字母组成 
#  beginWord != endWord 
#  wordList 中的所有字符串 互不相同 
#  
#  Related Topics 广度优先搜索 哈希表 字符串 👍 973 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from typing import List
from collections import deque


class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        word_set = set(wordList)
        if len(word_set) == 0 or endWord not in word_set:
            return 0

        if beginWord in word_set:
            word_set.remove(beginWord)

        queue = deque()
        queue.append(beginWord)

        visited = set()
        visited.add(beginWord)

        word_len = len(beginWord)
        step = 1
        while queue:
            current_size = len(queue)
            for i in range(current_size):
                word = queue.popleft()

                word_list = list(word)
                for j in range(word_len):
                    # 先保存，最后恢复
                    origin_char = word_list[j]

                    for k in range(26):
                        word_list[j] = chr(ord('a') + k)
                        next_word = ''.join(word_list)
                        if next_word in word_set:
                            if next_word == endWord:
                                return step + 1
                            if next_word not in visited:
                                queue.append(next_word)
                                # 注意：添加到队列以后，必须马上标记为已经访问
                                visited.add(next_word)
                    word_list[j] = origin_char  # 恢复
            step += 1
        return 0


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
    solution = Solution()
    res = solution.ladderLength(beginWord, endWord, wordList)
    print(res)
