'''
1. 堆的定义： 1.满足完全二叉树  2. 父节点值 > 子节点值 （大顶堆）， 父节点值 < 子节点值 （小顶堆）

基本思路：
1. 将无序序列构建成一个堆（以数组表示），升序选择大顶堆，降序选择小顶堆
2. 将堆顶元素与末尾元素交换，将最大元素沉到数组末尾
3. 重新调整结构，使其满足堆定义， 交换堆顶元素与末尾元素，反复执行调整+交换

几个公式：
1. parent = (i-1)//2
2. child1 = 2*i + 1
3. child2 = 2*i + 2

最优时间复杂度：O(n*log(n))，当keys 的值都不一样； O(n)，当keys 的值都一样
最坏时间复杂度：O(n*log(n))
平均时间复杂度：O(n*log(n))
'''


class HeapSort():
    # Time:NlogN n轮堆排序。每次构建大顶堆时，需要进行的比较和交换次数平均为logn
    # Space: O(1)
    # 不稳定:在堆排序中，会交换节点与子节点，如果有相等的数据，可能会改变相等数据的相对次序。
    def heap_sort(self, array):
        first = len(array) // 2 - 1
        for start in range(first, -1, -1):
            # 从下到上，从右到左对每个非叶节点进行调整，循环构建成大顶堆
            self.big_heap(array, start, len(array) - 1)
        for end in range(len(array) - 1, 0, -1):
            # 交换堆顶和堆尾的数据
            array[0], array[end] = array[end], array[0]
            # 重新调整完全二叉树，构造成大顶堆
            self.big_heap(array, 0, end - 1)
        return array

    def big_heap(self, array, start, end):
        root = start
        # 左孩子的索引
        child = root * 2 + 1
        while child <= end:
            # 节点有右子节点，并且右子节点的值大于左子节点，则将child变为右子节点的索引
            if child + 1 <= end and array[child] < array[child + 1]:
                child += 1
            if array[root] < array[child]:
                # 交换节点与子节点中较大者的值
                array[root], array[child] = array[child], array[root]
                # 交换值后，如果存在孙节点，则将root设置为子节点，继续与孙节点进行比较
                root = child
                child = root * 2 + 1
            else:
                break


class Solution(object):
    def heap_sort(self, nums):
        l = len(nums)
        self.nums = nums
        # 构造大顶堆，从非叶子节点开始倒序遍历，因此是l//2 -1 就是最后一个非叶子节点
        for i in range(l // 2 - 1, -1, -1):
            self.build_heap(i, l - 1)
        # 上面的循环完成了大顶堆的构造，那么就开始把根节点跟末尾节点交换，然后重新调整大顶堆
        for j in range(l - 1, -1, -1):
            nums[0], nums[j] = nums[j], nums[0]
            self.build_heap(0, j - 1)

        return nums

    def build_heap(self, i, l):
        """构建大顶堆： 构建以i为root的最大堆"""
        nums = self.nums
        root = i  # 父节点
        left, right = 2 * i + 1, 2 * i + 2  # 左右子节点的下标

        # 通过上面跟左右节点比较后，得出三个元素之间较大的下标
        if left <= l and nums[i] < nums[left]:
            root = left
        if right <= l and nums[left] < nums[right]:
            root = right

        # 如果较大值的下标不是父节点的下标，把最大值调换到root节点，
        # 交换后需要重新调整root节点下方，保证大顶堆。
        if root != i:
            nums[i], nums[root] = nums[root], nums[i]
            print(root, i, nums)
            self.build_heap(root, l)


if __name__ == "__main__":
    array = [10, 17, 50, 7, 30, 24, 27, 45, 15, 5, 36, 21]
    array = [4, 6, 7, 5, 9, 8, 3, 2]
    # heap_sort = HeapSort()
    heap_sort = Solution()
    print(heap_sort.heap_sort(array))
