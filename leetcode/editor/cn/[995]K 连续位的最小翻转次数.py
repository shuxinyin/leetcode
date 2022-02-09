# 在仅包含 0 和 1 的数组 A 中，一次 K 位翻转包括选择一个长度为 K 的（连续）子数组，同时将子数组中的每个 0 更改为 1，而每个 1 更改为 0
# 。 
# 
#  返回所需的 K 位翻转的最小次数，以便数组没有值为 0 的元素。如果不可能，返回 -1。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：A = [0,1,0], K = 1
# 输出：2
# 解释：先翻转 A[0]，然后翻转 A[2]。
#  
# 
#  示例 2： 
# 
#  
# 输入：A = [1,1,0], K = 2
# 输出：-1
# 解释：无论我们怎样翻转大小为 2 的子数组，我们都不能使数组变为 [1,1,1]。
#  
# 
#  示例 3： 
# 
#  
# 输入：A = [0,0,0,1,0,1,1,0], K = 3
# 输出：3
# 解释：
# 翻转 A[0],A[1],A[2]: A变成 [1,1,1,1,0,1,1,0]
# 翻转 A[4],A[5],A[6]: A变成 [1,1,1,1,1,0,0,0]
# 翻转 A[5],A[6],A[7]: A变成 [1,1,1,1,1,1,1,1]
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= A.length <= 30000 
#  1 <= K <= A.length 
#  
#  Related Topics 位运算 数组 前缀和 滑动窗口 👍 222 👎 0


# leetcode submit region begin(Prohibit modification and deletion)


class Solution:
    def minKBitFlips(self, nums, k):
        '''
        结论 1：后面区间的翻转，不会影响前面的元素。因此可以使用贪心策略，从左到右遍历，遇到每个 0 都把 它以及后面的 K−1 个元素进行翻转。
        结论 2：A[i] 翻转偶数次的结果是 A[i]；翻转奇数次的结果是 A[i] ^ 1。
        用一个队列q存储，当前位置i需要翻转时，则丢进队列q中，此时，i+k-1 则进行了翻转
           总结：当 A[i] 为 0，如果 i 位置被翻转了偶数次，那么翻转后仍是 0，当前元素需要翻转；
                当 A[i] 为 1，如果 i 位置被翻转了奇数次，那么翻转后变成 0，当前元素需要翻转。
        有总结可知  len(que) % 2 == A[i] 时，当前元素需要翻转。队列中元素的个数代表了i被前面 K−1个元素翻转的次数。
        '''
        import collections

        N = len(nums)
        res = 0
        que = collections.deque()

        for i in range(N - k + 1):
            # attention 检查当前位置是否超过了窗口大小，往右边滑动
            if que and i >= que[0] + k:
                que.popleft()
            if len(que) % 2 == nums[i]:
                if i + k > N:
                    return -1
                que.append(i)
                res += 1
        return res


# leetcode submit region end(Prohibit modification and deletion)
if __name__ == '__main__':
    A = [0, 0, 0, 1, 0, 1, 1, 0]
    K = 3
    S = Solution()
    print(S.minKBitFlips(A, K))
