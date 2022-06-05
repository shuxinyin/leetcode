class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return False

        p = 0
        for i in range(len(t)):
            if s[p] == t[i]:
                p += 1

            if p == len(s):
                return True
        return False


if __name__ == '__main__':
    s = "abc"
    t = "ahbgdc"

    S = Solution()
    print(S.isSubsequence(s, t))