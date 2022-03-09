# 按字典 wordList 完成从单词 beginWord 到单词 endWord 转化，一个表示此过程的 转换序列 是形式上像 beginWord -> 
# s1 -> s2 -> ... -> sk 这样的单词序列，并满足： 
# 
#  
#  
#  
#  每对相邻的单词之间仅有单个字母不同。 
#  转换过程中的每个单词 si（1 <= i <= k）必须是字典 wordList 中的单词。注意，beginWord 不必是字典 wordList 中的单
# 词。 
#  sk == endWord 
#  
# 
#  给你两个单词 beginWord 和 endWord ，以及一个字典 wordList 。请你找出并返回所有从 beginWord 到 endWord 的
#  最短转换序列 ，如果不存在这样的转换序列，返回一个空列表。每个序列都应该以单词列表 [beginWord, s1, s2, ..., sk] 的形式返回。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot",
# "log","cog"]
# 输出：[["hit","hot","dot","dog","cog"],["hit","hot","lot","log","cog"]]
# 解释：存在 2 种最短的转换序列：
# "hit" -> "hot" -> "dot" -> "dog" -> "cog"
# "hit" -> "hot" -> "lot" -> "log" -> "cog"
#  
# 
#  示例 2： 
# 
#  
# 输入：beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot",
# "log"]
# 输出：[]
# 解释：endWord "cog" 不在字典 wordList 中，所以不存在符合要求的转换序列。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= beginWord.length <= 5 
#  endWord.length == beginWord.length 
#  1 <= wordList.length <= 5000 
#  wordList[i].length == beginWord.length 
#  beginWord、endWord 和 wordList[i] 由小写英文字母组成 
#  beginWord != endWord 
#  wordList 中的所有单词 互不相同 
#  
#  
#  
#  Related Topics 广度优先搜索 哈希表 字符串 回溯 👍 545 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
from collections import deque


from collections import defaultdict
from typing import List
from collections import deque
import string


class Solution:

    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        # 先将 wordList 放到哈希表里，便于判断某个单词是否在 wordList 里
        word_set = set(wordList)
        res = []
        if len(word_set) == 0 or endWord not in word_set:
            return res

        successors = defaultdict(set)
        # 第 1 步：使用广度优先遍历得到后继结点列表 successors
        # key：字符串，value：广度优先遍历过程中 key 的后继结点列表

        found = self.__bfs(beginWord, endWord, word_set, successors)
        if not found:
            return res
        # 第 2 步：基于后继结点列表 successors ，使用回溯算法得到所有最短路径列表
        path = [beginWord]
        self.__dfs(beginWord, endWord, successors, path, res)
        return res

    def __bfs(self, beginWord, endWord, word_set, successors):
        queue = deque()
        queue.append(beginWord)

        visited = set()
        visited.add(beginWord)

        found = False
        word_len = len(beginWord)
        next_level_visited = set()

        while queue:
            current_size = len(queue)
            for i in range(current_size):
                current_word = queue.popleft()
                word_list = list(current_word)

                for j in range(word_len):
                    origin_char = word_list[j]

                    for k in string.ascii_lowercase:
                        word_list[j] = k
                        next_word = ''.join(word_list)

                        if next_word in word_set:
                            if next_word not in visited:
                                if next_word == endWord:
                                    found = True

                                # 避免下层元素重复加入队列
                                if next_word not in next_level_visited:
                                    next_level_visited.add(next_word)
                                    queue.append(next_word)

                                successors[current_word].add(next_word)
                    word_list[j] = origin_char
            if found:
                break
            # 取两集合全部的元素（并集，等价于将 next_level_visited 里的所有元素添加到 visited 里）
            visited |= next_level_visited
            next_level_visited.clear()
        return found

    def __dfs(self, beginWord, endWord, successors, path, res):
        if beginWord == endWord:
            res.append(path[:])
            return

        if beginWord not in successors:
            return

        successor_words = successors[beginWord]
        for next_word in successor_words:
            path.append(next_word)
            self.__dfs(next_word, endWord, successors, path, res)
            path.pop()


# leetcode submit region end(Prohibit modification and deletion)

if __name__ == '__main__':
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot", "dot", "dog", "lot", "log", "cog"]
    solution = Solution()
    res = solution.ladderLength(beginWord, endWord, wordList)
    print(res)

