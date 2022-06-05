class Solution:
    def firstUniqChar(self, s: str) -> str:
        # Time: O(N), Space: O(1)

        import collections
        dic = collections.OrderedDict()
        for c in s:
            dic[c] = True if c not in dic else False
        for k, v in dic.items():
            if v:
                return k
        return ' '


if __name__ == '__main__':
    s = "abaccdeff"
    S = Solution()
    print(S.firstUniqChar(s))
