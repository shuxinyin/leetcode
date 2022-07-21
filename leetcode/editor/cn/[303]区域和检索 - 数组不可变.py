# 给定一个整数数组 nums，处理以下类型的多个查询: 
# 
#  
#  计算索引 left 和 right （包含 left 和 right）之间的 nums 元素的 和 ，其中 left <= right 
#  
# 
#  实现 NumArray 类： 
# 
#  
#  NumArray(int[] nums) 使用数组 nums 初始化对象 
#  int sumRange(int i, int j) 返回数组 nums 中索引 left 和 right 之间的元素的 总和 ，包含 left 和 
# right 两点（也就是 nums[left] + nums[left + 1] + ... + nums[right] ) 
#  
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：
# ["NumArray", "sumRange", "sumRange", "sumRange"]
# [[[-2, 0, 3, -5, 2, -1]], [0, 2], [2, 5], [0, 5]]
# 输出：
# [null, 1, -1, -3]
# 
# 解释：
# NumArray numArray = new NumArray([-2, 0, 3, -5, 2, -1]);
# numArray.sumRange(0, 2); // return 1 ((-2) + 0 + 3)
# numArray.sumRange(2, 5); // return -1 (3 + (-5) + 2 + (-1)) 
# numArray.sumRange(0, 5); // return -3 ((-2) + 0 + 3 + (-5) + 2 + (-1))
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 10⁴ 
#  -10⁵ <= nums[i] <= 10⁵ 
#  0 <= i <= j < nums.length 
#  最多调用 10⁴ 次 sumRange 方法 
#  
#  Related Topics 设计 数组 前缀和 👍 482 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class NumArray:
    '''
        nums 数组的每一项都对应有它的前缀和： nums 的第 0 项到 当前项 的和。
        用数组 preSum 表示，preSum[i]：第 0 项到 第 i 项 的和。
            preSum[i]=nums[0]+nums[1]+…+nums[i]
        易得，nums 的某项 = 两个相邻前缀和的差：
            nums[i]=preSum[i]−preSum[i−1]
        对于 nums 的 i 到 j 的元素和，上式叠加，有：
            nums[i]+…+nums[j]=preSum[j]−preSum[i−1]
    '''

    def __init__(self, nums: List[int]):
        self.sums = [0]
        _sums = self.sums

        for num in nums:
            _sums.append(_sums[-1] + num)

    def sumRange(self, i: int, j: int) -> int:
        _sums = self.sums
        return _sums[j + 1] - _sums[i]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
# leetcode submit region end(Prohibit modification and deletion)
