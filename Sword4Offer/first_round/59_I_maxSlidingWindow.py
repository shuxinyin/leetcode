class Solution:
    def maxSlidingWindow(self, nums: [int], k: int) -> [int]:
        import collections
        if not nums or k == 0: return []
        deque = collections.deque()

        res = []
        i = 0
        while i < len(nums) and len(deque) < k:
            deque.append(nums[i])
            i += 1
            if len(deque) == k:
                x = max(deque)
                res.append(x)
                deque.popleft()
        return res

    def maxSlidingWindow2(self, nums: [int], k: int) -> [int]:
        import collections
        deque = collections.deque()
        res, n = [], len(nums)
        for i, j in zip(range(1 - k, n + 1 - k), range(n)):
            # 删除 deque 中对应的 nums[i-1]
            if i > 0 and deque[0] == nums[i - 1]:
                deque.popleft()
            # 保持 deque 递减
            while deque and deque[-1] < nums[j]:
                deque.pop()
            deque.append(nums[j])
            # 记录窗口最大值
            if i >= 0:
                res.append(deque[0])
        return res


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        import collections
        if not nums or k == 0: return []
        deque = collections.deque()
        # 未形成窗口
        for i in range(k):
            while deque and deque[-1] < nums[i]:
                deque.pop()
            deque.append(nums[i])
        res = [deque[0]]
        # 形成窗口后
        for i in range(k, len(nums)):
            if deque[0] == nums[i - k]:
                deque.popleft()
            while deque and deque[-1] < nums[i]:
                deque.pop()
            deque.append(nums[i])
            res.append(deque[0])
        return res


if __name__ == '__main__':
    S = Solution()
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    print(S.maxSlidingWindow2(nums, k))
