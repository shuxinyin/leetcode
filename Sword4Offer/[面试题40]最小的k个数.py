# 输入整数数组 arr ，找出其中最小的 k 个数。例如，输入4、5、1、6、2、7、3、8这8个数字，则最小的4个数字是1、2、3、4。 
# 
#  
# 
#  示例 1： 
# 
#  输入：arr = [3,2,1], k = 2
# 输出：[1,2] 或者 [2,1]
#  
# 
#  示例 2： 
# 
#  输入：arr = [0,1,2,1], k = 1
# 输出：[0] 
# 
#  
# 
#  限制： 
# 
#  
#  0 <= k <= arr.length <= 10000 
#  0 <= arr[i] <= 10000 
#  
#  Related Topics 数组 分治 快速选择 排序 堆（优先队列） 👍 451 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        # 数组划分:对这 k 个数的顺序并没有要求。
        # 因此，只需要将数组划分为 最小的k个数 和 其他数字 两部分即可，而快速排序的哨兵划分可完成此目标
        # 根据快速排序原理，如果某次哨兵划分后基准数正好是第k + 1小的数字 ，那么此时基准数左边的所有数字便是题目所求的最小的k个数 。
        # Time: O(N), Space: O(logN)
        if k >= len(arr): return arr

        def quick_sort(l, r):
            i, j = l, r
            while i < j:
                while i < j and arr[j] >= arr[l]: j -= 1
                while i < j and arr[i] <= arr[l]: i += 1
                arr[i], arr[j] = arr[j], arr[i]
            arr[l], arr[i] = arr[i], arr[l]
            if k < i: return quick_sort(l, i - 1)
            if k > i: return quick_sort(i + 1, r)
            return arr[:k]

        return quick_sort(0, len(arr) - 1)

# leetcode submit region end(Prohibit modification and deletion)
