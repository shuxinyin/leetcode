class QuickSort():
    def quick_sort(self, nums, l, r):
        # Time: O(Nlog(N))，最坏时间复杂度O(N*N)
        # Space: O(N)
        # 快速排序的递归深度最好（平均）为 O(logN)，最差情况O(N)（即输入数组完全倒序)。
        # 不稳定
        if l >= r:
            return nums
        i, j = l, r
        pivot = nums[l]  # 选定标杆
        while i < j:
            while i < j and nums[j] >= pivot:  # 在右边找比pivot小的，找到即停止
                j -= 1
            while i < j and nums[i] <= pivot:  # 在左边找比pivot大的，找到即停止
                i += 1
            nums[i], nums[j] = nums[j], nums[i]
        nums[l], nums[i] = nums[i], nums[l]  # 把标杆插到中间，左边都是 < pivot, 右边都是 > pivot
        self.quick_sort(nums, l, i - 1)
        self.quick_sort(nums, i + 1, r)
        return nums


if __name__ == "__main__":
    nums = [13, 19, 5, 12, 8, 7, 4, 21, 6, 11]
    nums = [30, 24, 5, 58, 18, 36, 12, 42, 39]
    quick_sort = QuickSort()
    print(quick_sort.quick_sort(nums, 0, len(nums) - 1))
