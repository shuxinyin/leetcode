class Solution:
    def reverseLeftWords(self, s: str, n: int) -> str:
        # Time: O(N), Space: O(N)

        s1 = s[:n]
        s2 = s[n:]

        return s2 + s1


if __name__ == '__main__':
    S = Solution()
    print(S.reverseLeftWords("abcdefg", 2))

    s = "abcdefg"
    print(s[:2])
