# 给你一个整数数组 nums ，你可以对它进行一些操作。 
# 
#  每次操作中，选择任意一个 nums[i] ，删除它并获得 nums[i] 的点数。之后，你必须删除 所有 等于 nums[i] - 1 和 nums[i]
#  + 1 的元素。 
# 
#  开始你拥有 0 个点数。返回你能通过这些操作获得的最大点数。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [3,4,2]
# 输出：6
# 解释：
# 删除 4 获得 4 个点数，因此 3 也被删除。
# 之后，删除 2 获得 2 个点数。总共获得 6 个点数。
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = [2,2,3,3,3,4]
# 输出：9
# 解释：
# 删除 3 获得 3 个点数，接着要删除两个 2 和 4 。
# 之后，再次删除 3 获得 3 个点数，再次删除 3 获得 3 个点数。
# 总共获得 9 个点数。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 2 * 10⁴ 
#  1 <= nums[i] <= 10⁴ 
#  
#  Related Topics 数组 哈希表 动态规划 👍 638 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def deleteAndEarn(self, nums: [int]) -> int:
        '''转化为打家劫舍问题
        nums = [2,2,3,3,3,4]  ->  count_list = [0,0,2,3,1]，index表示num=2有有两个，num=3有三个...
        这样就转化为打家劫舍问题，不能选邻居点
        状态： dp[i]表示删除第i个数时达到的最高点数
        转移： dp[i] = max(dp[i-1], dp[i-2]+count_list[i]*i)  # 不偷i位置 或 选偷i位置
        初始状态：dp[0] = 0， dp[1] =  count_list[1]
        '''
        if not nums:
            return 0

        n = max(nums)
        count_list = [0] * (n + 1)
        for num in nums:
            count_list[num] += 1

        dp = [0] * (n + 1)
        dp[1] = count_list[1]
        for i in range(2, n + 1):
            dp[i] = max(dp[i - 1], dp[i - 2] + count_list[i] * i)
        return dp[-1]

    def deleteAndEarn2(self, nums: List[int]) -> int:
        '''降空间 O(1)
        '''
        if not nums:
            return 0

        n = max(nums)
        A = [0] * (n + 1)
        for num in nums:
            A[num] += 1

        pre, cur = 0, A[1]
        for i in range(2, n + 1):
            pre, cur = cur, max(pre + A[i]*i, cur)
        return cur

# leetcode submit region end(Prohibit modification and deletion)

if __name__ == '__main__':
    nums = [2, 2, 3, 3, 3, 4]
    S = Solution()
    print(S.deleteAndEarn(nums))
