class QuickSort():
    def quick_sort(self, lists, l, r):
        # Time: O(Nlog(N))
        # Space: O(N)：快速排序的递归深度最好（平均）为 O(logN)，最差情况（即输入数组完全倒序为O(N)。
        # 不稳定
        if l >= r:
            return list
        i, j = l, r
        pivot = lists[l]
        while i < j:
            while i < j and lists[j] >= pivot:
                j -= 1
            while i < j and lists[i] <= pivot:
                i += 1
            lists[i], lists[j] = lists[j], lists[i]
        lists[l], lists[i] = lists[i], lists[l]
        self.quick_sort(lists, l, i - 1)
        self.quick_sort(lists, i + 1, r)
        return lists






if __name__ == "__main__":
    lists = [13, 19, 5, 12, 8, 7, 4, 21, 6, 11]
    lists = [30, 24, 5, 58, 18, 36, 12, 42, 39]
    quick_sort = QuickSort()
    print(quick_sort.quick_sort(lists, 0, len(lists) - 1))

