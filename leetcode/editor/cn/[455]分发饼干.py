# 假设你是一位很棒的家长，想要给你的孩子们一些小饼干。但是，每个孩子最多只能给一块饼干。 
# 
#  对每个孩子 i，都有一个胃口值 g[i]，这是能让孩子们满足胃口的饼干的最小尺寸；并且每块饼干 j，都有一个尺寸 s[j] 。如果 s[j] >= g[
# i]，我们可以将这个饼干 j 分配给孩子 i ，这个孩子会得到满足。你的目标是尽可能满足越多数量的孩子，并输出这个最大数值。 
#  
# 
#  示例 1: 
# 
#  
# 输入: g = [1,2,3], s = [1,1]
# 输出: 1
# 解释: 
# 你有三个孩子和两块小饼干，3个孩子的胃口值分别是：1,2,3。
# 虽然你有两块小饼干，由于他们的尺寸都是1，你只能让胃口值是1的孩子满足。
# 所以你应该输出1。
#  
# 
#  示例 2: 
# 
#  
# 输入: g = [1,2], s = [1,2,3]
# 输出: 2
# 解释: 
# 你有两个孩子和三块小饼干，2个孩子的胃口值分别是1,2。
# 你拥有的饼干数量和尺寸都足以让所有孩子满足。
# 所以你应该输出2.
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= g.length <= 3 * 10⁴ 
#  0 <= s.length <= 3 * 10⁴ 
#  1 <= g[i], s[j] <= 2³¹ - 1 
#  
#  Related Topics 贪心 数组 排序 👍 421 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findContentChildren(self, g, s) -> int:
        '''
        贪心思想： 从胃口最小的小孩子满足起，分配最小且能满足胃口的饼干，则每一步都是最好的安排
        解题思路：
            此处不要第一想法想着用for循环。
            采用两个index，ind1标记g,ind2标记s
            while 做一个判断循环即可

        时间复杂度： 排序O(nlogn) + n
        '''

        g.sort()
        s.sort()
        k = 0
        ind1, ind2 = 0, 0
        while ind1 < len(g) and ind2 < len(s):
            if g[ind1] <= s[ind2]:
                k += 1
                ind1 += 1
                ind2 += 1
            else:
                ind2 += 1
        return k


# leetcode submit region end(Prohibit modification and deletion)

if __name__ == "__main__":
    S = Solution()
    res = S.findContentChildren([1, 2, 3], [1, 1])
    print(res)
