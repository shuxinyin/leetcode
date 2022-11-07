## DD-二分法

```python      
class DoubleDividedPattern:
    @staticmethod
    def pattern(cls, target):
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = l + (r - l) // 2
            if nums[mid] <= target:
                l = mid + 1
            else:
                r = mid - 1
        return l  # l永远是大于target的下一个数
```

[33]搜索旋转排序数组
[81]搜索旋转排序数组 II

[34]在排序数组中查找第一个和最后一个位置
[35]搜索插入位置

[69]x 的平方根 

[153]寻找旋转排序数组中的最小值
[154]寻找旋转排序数组中的最小值 II

[540]有序数组中的单一元素
[4]寻找两个正序数组的中位数



#### [33]搜索旋转排序数组
> 整数数组 nums 按升序排列，数组中的值 互不相同 。 
>  在传递给函数之前，nums 在预先未知的某个下标 k（0 <= k < nums.length）上进行了 旋转，使数组变为 [nums[k], nums[
> k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]（下标 从 0 开始 计数）。例如， [0,1,2
> ,4,5,6,7] 在下标 3 处经旋转后可能变为 [4,5,6,7,0,1,2] 。 
>  给你 旋转后 的数组 nums 和一个整数 target ，如果 nums 中存在这个目标值 target ，则返回它的下标，否则返回 -1 。 
> 
>  示例 1： 
> 输入：nums = [4,5,6,7,0,1,2], target = 0
> 输出：4


```python
class Solution:
    def search(self, nums, target):
        '''
        将数组一分为二，其中一定有一个是有序的，另一个可能是有序，也能是部分有序。
        此时有序部分用二分法查找。
        无序部分再一分为二，其中一个一定有序，另一个可能有序，可能无序。就这样循环.
        '''
        l, r = 0, len(nums)-1

        while l<=r:
            mid = l + (r-l)//2
            if nums[mid] == target:
                return mid
            
            # [l, mid], [mid, r]
            if nums[l] <= nums[mid]:  # 左边有序
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            else:
                if nums[mid] < target <= nums[len(nums)-1]:
                    l = mid +1
                else:
                    r = mid -1
        return -1

```
#### [81]搜索旋转排序数组 II

> 已知存在一个按非降序排列的整数数组 nums ，数组中的值不必互不相同。 
> 
>  在传递给函数之前，nums 在预先未知的某个下标 k（0 <= k < nums.length）上进行了 旋转 ，使数组变为 [nums[k], 
> nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]（下标 从 0 开始 计数）。例如， [0,1,
> 2,4,4,4,5,6,6,7] 在下标 5 处经旋转后可能变为 [4,5,6,6,7,0,1,2,4,4] 。 
> 
>  给你 旋转后 的数组 nums 和一个整数 target ，请你编写一个函数来判断给定的目标值是否存在于数组中。如果 nums 中存在这个目标值 
> target ，则返回 true ，否则返回 false 。 
> 
>  你必须尽可能减少整个操作步骤。 
> 
>  示例 1： 
> 输入：nums = [2,5,6,0,0,1,2], target = 0
> 输出：true


```python
class Solution(object):
    def search(self, nums, target):
        """
        相比于33-搜索旋转排序数组I，多了这一种情况[1, 1, 2, 1] 需要考虑
        """
        n = len(nums)
        i, j = 0, n-1
        while i <= j:  # 终止条件
            mid = i + (j - i) // 2  # 中间数下标
            if nums[mid] == target:
                return True
            elif nums[mid] > nums[i]:  # 前半部分有序
                if nums[i] <= target < nums[mid]:  # 目标值处在前半部分，移动的部分不加等号
                    j = mid - 1
                else:  # 目标值处在后半部分
                    i = mid + 1
            elif nums[mid] < nums[i]:  # 后半部分有序
                if nums[mid] < target <= nums[j]:
                    i = mid + 1
                else:
                    j = mid - 1
            elif nums[mid] == nums[i]:  #  [1, 0, 1, 1, 1]
                i += 1  # 无法判断哪边有序， i+1,排序一个错误选项
```

#### [34]在排序数组中查找第一个和最后一个位置
> 给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。 
>  如果数组中不存在目标值 target，返回 [-1, -1]。 
>  进阶： 
>  你可以设计并实现时间复杂度为 O(log n) 的算法解决此问题吗？ 
>  
>  示例 1： 
> 输入：nums = [5,7,7,8,8,10], target = 8
> 输出：[3,4] 

```python
class Solution:
    def searchRange(self, nums, target):
        n = len(nums)
        l, r = 0, n-1
        
        while l <= r:
            mid = l + (r-l) // 2

            if nums[mid] <= target:
                l = mid +1
            else:
                r = mid -1
        return l

class Solution:
    def searchRange(self, nums, target):
        '''
        考虑 target开始和结束位置，
        其实我们要找的就是数组中「第一个等于 target的位置」（记为leftIdx）
        和「第一个大于 target的位置减一」（记为rightIdx）。
        '''
        if len(nums) == 0:
            return [-1, -1]

        first_position = self.find_first_position(nums, target)
        if first_position == -1:
            return [-1, -1]
        last_position = self.find_last_position(nums, target)
        return [first_position, last_position-1]

    def find_first_position(self, nums, target):
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] == target:
                right = mid  # ATTENTION，找左边界，移动right，向左走
            else:
                # nums[mid] > target
                right = mid - 1

        if nums[left] == target:
            return left
        else:
            return -1

    def find_last_position(self, nums, target):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right + 1) // 2
            if nums[mid] > target:
                right = mid - 1
            else:
                # nums[mid] < target
                left = mid + 1

        # 由于能走到这里，说明在数组中一定找得到目标元素，因此这里不用再做一次判断
        return left
```

#### [35]搜索插入位置
> 给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。
> 请必须使用时间复杂度为 O(log n) 的算法。 
> 示例 1: 
> 输入: nums = [1,3,5,6], target = 5
> 输出: 2

```python
class Solution:
    def searchInsert(self, nums, target):
        n = len(nums)
        if n <= 1:
            return 
        
        l, r = 0, n -1
        while l <= r:
            mid = l + (r-l)//2

            if nums[mid] <=target:
                l = mid + 1
            else:
                r = mid -1
        if l >= n:  # target > nums[r]情形
            return l
        else:
            return  l - 1
```

#### [69]x 的平方根 

> 给你一个非负整数 x ，计算并返回 x 的 算术平方根 。 
>  由于返回类型是整数，结果只保留 整数部分 ，小数部分将被 舍去 。  
>  注意：不允许使用任何内置指数函数和算符，例如 pow(x, 0.5) 或者 x ** 0.5 。 
>  示例 1： 
> 输入：x = 4
> 输出：2

```python
class Solution:
    def mySqrt(self, x):
        l, r = 0, x

        while l<=r:
            mid = l + (r - l) // 2

            if mid*mid <= x:
                l = mid + 1
            else:
                r = mid + 1
        return l - 1
```

#### [153]寻找旋转排序数组中的最小值
> 已知一个长度为 n 的数组，预先按照升序排列，经由 1 到 n 次 旋转 后，得到输入数组。例如，原数组 nums = [0,1,2,4,5,6,7] 在变
> 化后可能得到：
>  若旋转 4 次，则可以得到 [4,5,6,7,0,1,2] 
>  若旋转 7 次，则可以得到 [0,1,2,4,5,6,7] 
>  注意，数组 [a[0], a[1], a[2], ..., a[n-1]] 旋转一次 的结果为数组 [a[n-1], a[0], a[1], a[2], 
> ..., a[n-2]] 。 
>  给你一个元素值 互不相同 的数组 nums ，它原来是一个升序排列的数组，并按上述情形进行了多次旋转。请你找出并返回数组中的 最小元素 。 
>  示例 1： 
> 输入：nums = [3,4,5,1,2]
> 输出：1
> 解释：原数组为 [1,2,3,4,5] ，旋转 3 次得到输入数组。

```python
class Solution:
    def findMin(self, nums):
        ''' 数组的最后一个元素x，在最小值右侧的元素，均 < x, 而最小值左侧的元素严格大于x
        最小值只存在两种情况，
        一种存在于左边， 则 r = mid
        一种存在于右边， 则 l = mid + 1
        '''
        n = len(nums)
        l, r = 0, n-1

        while l < r:
            mid = l + (r - l) // 2
            if nums[mid] < nums[r]:  # 说明最小元素在[l, mid]
                r = mid
            else:
                l = mid + 1   # 说明最小元素在(mid, r]
        return nums[l]
```

#### [154]寻找旋转排序数组中的最小值 II
> 已知一个长度为 n 的数组，预先按照升序排列，经由 1 到 n 次 旋转 后，得到输入数组。例如，原数组 nums = [0,1,4,4,5,6,7] 在变
> 化后可能得到：
>  若旋转 4 次，则可以得到 [4,5,6,7,0,1,4] 
>  若旋转 7 次，则可以得到 [0,1,4,4,5,6,7] 
>  注意，数组 [a[0], a[1], a[2], ..., a[n-1]] 旋转一次 的结果为数组 [a[n-1], a[0], a[1], a[2], 
> ..., a[n-2]] 。 
>  给你一个可能存在 重复 元素值的数组 nums ，它原来是一个升序排列的数组，并按上述情形进行了多次旋转。请你找出并返回数组中的 最小元素 。 
>  示例 1： 
> 输入：nums = [1,3,5]
> 输出：1

```python
class Solution:
    def findMin(self, nums):
        # nums可能存在重复元素值的数组
        '''
        最小值只存在两种情况，
        一种存在于左边， 则 r = mid
        一种存在于右边， 则 l = mid + 1
        一种nums[mid]=nums[l]=nums[r], 则r-=1, 因为nums[r]可被nums[mid]替代
        '''
        n = len(nums)
        l, r = 0, n

        while l < r:
            mid = l + (r - l) // 2
            if nums[mid] < nums[r]:  # 说明最小元素在[l, mid]
                r = mid
            elif nums[mid] > nums[r]:
                l = mid + 1  # 说明最小元素在[mid, r]
            else:
                r = r - 1  # [4, 4, 1, 4]
        return nums[l]
```

#### [540]有序数组中的单一元素
> 给你一个仅由整数组成的有序数组，其中每个元素都会出现两次，唯有一个数只会出现一次。 
>  请你找出并返回只出现一次的那个数。  
>  你设计的解决方案必须满足 O(log n) 时间复杂度和 O(1) 空间复杂度。 
> 示例 1: 
> 输入: nums = [1,1,2,3,3,4,4,8,8]
> 输出: 2

```python
class Solution:
    def singleNonDuplicate(self, nums):
        '''
        由于给定数组有序 且 常规元素总是两两出现，因此如果不考虑“特殊”的单一元素的话，
        有结论：成对元素中的第一个所对应的下标必然是偶数，成对元素中的第二个所对应的下标必然是奇数。
        然后再考虑存在单一元素的情况，假如单一元素所在的下标为 xxx，那么下标 xxx 之前（左边）的位置仍满足上述结论，
        而下标 xxx 之后（右边）的位置由于 xxx 的插入，导致结论翻转。

        利用按位异或的性质，可以得到mid和相邻的数之间的如下关系，其中 ⊕是按位异或运算符：
        当mid是偶数时，mid+1=mid⊕1；
        当mid是奇数时，mid−1=mid⊕1。  
        因此在二分查找的过程中，不需要判断 mid的奇偶性。
        '''
        n = len(nums)
        l, r = 0, n-1

        while l < r:
            mid = l + (r - l) // 2

            if mid % 2 == 1:  # 保持mid 为偶数
                mid = mid - 1  

            if nums[mid] = nums[mid + 1]:
                l = mid + 2
            else:  # 说明mid之前存在单个，r前移到mid处
                r=mid
        return nums[l]

```


#### [4]寻找两个正序数组的中位数

> 给定两个大小分别为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。请你找出并返回这两个正序数组的 中位数。
> 算法的时间复杂度应该为 O(log (m+n)) 。
> 示例 1： 
> 输入：nums1 = [1,3], nums2 = [2]
> 输出：2.00000
> 解释：合并数组 = [1,2,3] ，中位数 2

```python
class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        


```