# 给定一个数组 nums 和滑动窗口的大小 k，请找出所有滑动窗口里的最大值。 
# 
#  示例: 
# 
#  输入: nums = [1,3,-1,-3,5,3,6,7], 和 k = 3
# 输出: [3,3,5,5,6,7] 
# 解释: 
# 
#   滑动窗口的位置                最大值
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
#  1 [3  -1  -3] 5  3  6  7       3
#  1  3 [-1  -3  5] 3  6  7       5
#  1  3  -1 [-3  5  3] 6  7       5
#  1  3  -1  -3 [5  3  6] 7       6
#  1  3  -1  -3  5 [3  6  7]      7 
# 
#  
# 
#  提示： 
# 
#  你可以假设 k 总是有效的，在输入数组不为空的情况下，1 ≤ k ≤ 输入数组的大小。 
# 
#  注意：本题与主站 239 题相同：https://leetcode-cn.com/problems/sliding-window-maximum/ 
#  Related Topics 队列 滑动窗口 单调队列 堆（优先队列） 👍 470 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ''' 双边队列
            维持一个长度为k的窗口deque，原则，保持头部head元素最大
                1. 下一个元素比tail大， 则一直pop，后append
                2. 同时 判断head是否已经出窗口了
        '''
        from collections import deque
        if not nums or k == 0:
            return []

        n = len(nums)
        window = deque()
        res = []

        # 窗口未形成
        for i in range(n):
            while window and nums[i] > window[-1]:
                window.pop()
            window.append(nums[i])
        res.append(window[0])

        # 窗口已结形成
        for i in range(n):
            # 判断当前队列最大值head 是否已经出窗口了
            if window[0] == nums[i-k]:
                window.popleft()

            while window and nums[i] > window[-1]:
                window.pop()
            window.append(nums[i])
            res.append(window[0])
        return res

# leetcode submit region end(Prohibit modification and deletion)
