'''
平均时间复杂度：O(nlogn)
最佳时间复杂度：O(n)
最差时间复杂度：O(nlogn)
空间复杂度：O(n)
排序方式：In-place
稳定性：稳定
'''


class MergeSort():
    # 定义合并merge函数
    def merge(self, left_nums, right_nums):
        i, j = 0, 0
        res = []  # 存放left_nums与right_nums的合并内容
        while i < len(left_nums) and j < len(right_nums):
            # 如果左边的数大于右边的数，就将左边的数先添加到res中，再继续比较（合并的right_nums、left_nums已经排过序）
            # 反之如果如果右边的数大于左边的数，就将右边的数先添加到res中，再继续比较（合并的right_nums、left_nums已经排过序）
            if left_nums[i] <= right_nums[j]:
                res.append(left_nums[i])
                i += 1
            else:
                res.append(right_nums[j])
                j += 1
        # 因为当 i == len(left_nums) 或者 j == len(right_nums)时，跳出while循环，
        # 对未处理完的一个列表，直接加入res中
        if i == len(left_nums):
            res += right_nums[j:]
        else:
            res += left_nums[i:]
        return res

    # 定义排序merge_sort函数
    def merge_sort(self, nums):
        length = len(nums)
        if length <= 1:
            return nums
        else:
            # 分：1.将整个数组对半分开，直到只剩一个元素
            #    2.从一个元素开始往回进行对比合并，将合并的内容暂且放在一个空列表中
            mid = length // 2
            left = self.merge_sort(nums[:mid])
            right = self.merge_sort(nums[mid:])
            return self.merge(left, right)


class MergeSort_repeat():
    def merge(self, left, right):

        res = []
        i = j = 0
        while i <= len(left) and j <= len(right):
            if left[i] <= right[j]:
                res.append(nums[i])
                i += 1
            else:
                res.append(nums[j])
                j += 1

        if i == len(left):
            res += right[j:]
        else:
            res += left[i:]
        return res

    def merge_sort(self, nums):
        n = len(nums)
        if n <= 1:
            return nums
        mid = n // 2
        left = self.merge_sort(nums[:mid])
        right = self.merge_sort(nums[mid:])

        return self.merge(left, right)


if __name__ == '__main__':
    nums = [9, 8, 7, 5, 3, 6, 11, 2, 4, 1, 12]

    S = MergeSort()
    print(S.merge_sort(nums))
