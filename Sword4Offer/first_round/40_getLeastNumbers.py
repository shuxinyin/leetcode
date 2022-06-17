class Solution:
    def getLeastNumbers(self, arr: [int], k: int) -> [int]:
        def quick_sort(arr, l, r):
            # Time: O(NlogN), Space: O(N)
            if l >= r:
                return

            pivot = arr[l]
            i, j = l, r
            while i < j:
                while i < j and arr[j] >= pivot:
                    j -= 1
                while i < j and arr[i] <= pivot:
                    i += 1
                arr[i], arr[j] = arr[j], arr[i]
            arr[l], arr[i] = arr[i], arr[l]
            quick_sort(arr, l, i - 1)
            quick_sort(arr, i + 1, r)

        quick_sort(arr, 0, len(arr) - 1)
        return arr[:k]

    def getLeastNumbers2(self, arr: [int], k: int) -> [int]:
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


if __name__ == '__main__':
    S = Solution()

    l = [3, 2, 1]
    k=2
    print(S.getLeastNumbers(l, 2))
