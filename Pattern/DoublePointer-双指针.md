## DoublePointer-双指针法

```python      
class DoubleDividedPattern:
    @staticmethod
    def pattern(cls, nums, target):
        n = len(nums)
        if n <= 2:
            return

        l, r = 0, 1
        while r < n:
            if nums[l] == nums[r]:
                r += 1
            else:
                l += 1
                nums[l] = nums[r]
        return l + 1
```

几个数之和
[1]两数之和
[15]三数之和
[16]最接近的三数之和
[18]四数之和

[11]盛水最多的容器
[35]接雨水

原地修改数组
[26]去除数组中重复的数字
[27]移除元素
[31]下一个排列

[88]归并两个排序数组
[142]快慢指针
[633]平方数之和

[680]验证回文字符串II
[524]通过删除字母匹配到字典里最长单词

#### 几个数之和

#### [1]两数之和

> 给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出 和为目标值 target 的那 两个
> 整数，并返回它们的数组下标。  
> 你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。
> 你可以按任意顺序返回答案。
> 示例 1：
> 输入：nums = [2,7,11,15], target = 9
> 输出：[0,1]
> 解释：因为 nums[0] + nums[1] == 9 ，返回 [0, 1] 。

```python
class Solution:
    def twoSum(self, nums, target):
        '''
        先排序，双指针滑动方法。
        '''
        d = {}
        n = len(nums)
        for i in range(n):
            if target - nums[i] in d:
                return d[target - nums[i]], i
            else:
                d[nums[i]] = i

```

#### [15]三数之和

> 给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有和为 0 且不重
> 复的三元组。
> 注意：答案中不可以包含重复的三元组。
> 示例 1：
> 输入：nums = [-1,0,1,2,-1,-4]
> 输出：[[-1,-1,2],[-1,0,1]]

```python
class Solution:
    def threeSum(self, nums):
        '''
        Sort + Double_Pointer
        1.数组从小到大排序
        2.遍历数组（k），取l，r两个滑动指针， k<l<r
        3.取s=nums[k]+nums[l]+nums[r]
        4.while(l<r)分3类：
            a.s<0: l++
            b.s>0: r--
            c.s==0: 添加此组合（k,l,r）, l,r继续滑动，寻找还有没有其他结果
        '''
        nums = sorted(nums)
        res = []
        for k in range(len(nums) - 2):
            if nums[k] > 0: break
            if k > 0 and nums[k] == nums[k - 1]: continue
            l, r = k + 1, len(nums) - 1
            while l < r:
                print(l, r)
                tmp = nums[k] + nums[l] + nums[r]
                if tmp < 0:
                    l += 1
                    # 重复的值跳过
                    while l < r and nums[l] == nums[l - 1]: l += 1
                elif tmp > 0:
                    r -= 1
                    # 重复的值跳过
                    while l < r and nums[r] == nums[r + 1]: r -= 1
                else:
                    res.append([nums[k], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    # 重复的值跳过
                    while l < r and nums[l] == nums[l - 1]: l += 1
                    while l < r and nums[r] == nums[r + 1]: r -= 1
        return res
```

#### [16]最接近的三数之和

> 给你一个长度为 n 的整数数组 nums 和 一个目标值 target。请你从 nums 中选出三个整数，使它们的和与 target 最接近。
> 返回这三个数的和。
> 假定每组输入只存在恰好一个解。
> 示例 1：
> 输入：nums = [-1,2,1,-4], target = 1
> 输出：2
> 解释：与 target 最接近的和是 2 (-1 + 2 + 1 = 2) 。

```python
class Solution:
    def threeSumClosest(self, nums, target):
        '''
        Sort + Double_Pointer
        1. 首先定义res-target无限大，第一步让res等于第一个组合的sum
        2. 剩下就分为三类情况，
            2.1 sum < target: l+=1
            2.1 sum > target: r-=1
            2.1 sum = target: return sum
        '''
        nums = sorted(nums)
        res = float("inf")
        for k in range(len(nums) - 2):
            l, r = k + 1, len(nums) - 1
            while l != r:
                tmp = nums[l] + nums[k] + nums[r]
                if abs(res - target) >= abs(tmp - target):
                    res = tmp
                if tmp - target < 0:
                    l += 1
                    # nums[left]重复值，则跳过
                    while l != r and nums[l] == nums[l - 1]:
                        l += 1
                elif tmp - target > 0:
                    r -= 1
                    # nums[right]重复值，则跳过
                    while l != r and nums[r] == nums[r + 1]:
                        r -= 1
                else:
                    return tmp

        return res
```

#### [18]四数之和

> 给你一个由 n 个整数组成的数组 nums ，和一个目标值 target 。请你找出并返回满足下述全部条件且不重复的四元组 [nums[a],
> nums[
> b], nums[c], nums[d]] （若两个四元组元素一一对应，则认为两个四元组重复）：
> 0 <= a, b, c, d < n
> a、b、c 和 d 互不相同
> nums[a] + nums[b] + nums[c] + nums[d] == target
> 你可以按 任意顺序 返回答案 。
> 示例 1：
> 输入：nums = [1,0,-1,0,-2,2], target = 0
> 输出：[[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]

```python
class Solution:
    def fourSum(self, nums, target):
        nums = sorted(nums)

        res = []
        length = len(nums)
        for i in range(length - 3):
            if i > 0 and nums[i] == nums[i - 1]:  # 当i的值与前面的值相等时忽略
                continue
            # 获取当前最小值,如果最小值比目标值大,说明后面越来越大的值根本没戏
            if nums[i] + nums[i + 1] + nums[i + 2] + nums[i + 3] > target:
                break  # 这里使用的break,直接退出此次循环,因为后面的数只会更大
            # 获取当前最大值,如果最大值比目标值小,说明后面越来越小的值根本没戏,忽略
            if nums[i] + nums[length - 3] + nums[length - 2] + nums[length - 1] < target:
                continue  # 这里使用continue,继续下一次循环,因为下一次循环有更大的数

            for j in range(i + 1, length - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:  # 当j的值与前面的值相等时忽略
                    continue
                if nums[i] + nums[j] + nums[j + 1] + nums[j + 2] > target:
                    break
                if nums[i] + nums[j] + nums[length - 2] + nums[length - 1] < target:
                    continue

                l, r = j + 1, length - 1
                while l < r:
                    s = nums[i] + nums[j] + nums[l] + nums[r]
                    if s < target:
                        l += 1
                        # 去重复值，跳过
                        while l < r and nums[l] == nums[l - 1]:
                            l += 1
                    elif s > target:
                        r -= 1
                        # 去重复值，跳过
                        while l < r and nums[r] == nums[r + 1]:
                            r -= 1
                    else:
                        res.append([nums[i], nums[j], nums[l], nums[r]])
                        l += 1
                        r -= 1
                        # 去重复值，跳过
                        while l < r and nums[l] == nums[l - 1]:
                            l += 1
                        while l < r and nums[r] == nums[r + 1]:
                            r -= 1
        return res
```

#### [11]盛水最多的容器

> 给你 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i,
> ai) 和 (i, 0) 。找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。
> 说明：你不能倾斜容器。
> 示例 1：
> 输入：[1,8,6,2,5,4,8,3,7]
> 输出：49
> 解释：图中垂直线代表输入数组 [1,8,6,2,5,4,8,3,7]。在此情况下，容器能够容纳水（表示为蓝色部分）的最大值为 49。

```python
class Solution:
    def maxArea(self, height):
        '''
        关键在于： 永远只能左右两个边，不论移动那边，底会减小
                 要想面积增大，只能移动矮的那边，才可能增大
        '''
        res = -1
        l, r = 0, len(height) - 1
        while l < r:
            tmp = min(height[l], height[r]) * (r - l)
            if res < tmp:
                res = tmp
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return res
```

#### [35]接雨水

> 给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
> 示例 1：
> 输入：height = [0,1,0,2,1,0,1,3,2,1,2,1]
> 输出：6
> 解释：上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。

```python
class Solution:
    ''' DoublePointer
    按竖列单个算:（造一个局部凹凸点）：
    左边取一个最大高度max_left, 右边取一个最大高度max_left，单独算每一个竖列位置i能装多少水
    分两种情况：1. max_left <= i <= max_right： 无法接水
            2. i < min(max_right，max_left) ： 接水量 min(max_left, max_right) - h[i]
    '''

    def trap(self, height):
        # 边界条件
        if not height: return 0
        n = len(height)

        left, right = 1, n - 2  # 分别位于输入数组的两端
        max_left, max_right = height[0], height[n - 1]
        res = 0

        while left <= right:
            max_left = max(height[left], max_left)
            max_right = max(height[right], max_right)
            # 下面这两种情况,保证了现在在计算的位置一定是不大于左右的，保证了局部最小
            # 这样就免去了，每个位置都去搜索全局最大（如方法2）
            # 1.保证了 h[left]<=max_left<max_right
            # 2.保证了 h[right]<=max_right<max_left
            if max_left < max_right:
                res += max_left - height[left]
                left += 1
            else:
                res += max_right - height[right]
                right -= 1

        return res
```

#### 原地修改数组

#### [26]去除数组中重复的数字

> 给你一个有序数组 nums ，请你 原地 删除重复出现的元素，使每个元素 只出现一次， 返回删除后数组的新长度。
> 不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。
> 说明:
> 为什么返回数值是整数，但输出的答案是数组呢?
> 请注意，输入数组是以「引用」方式传递的，这意味着在函数里修改输入数组对于调用者是可见的。
> 你可以想象内部操作如下:
> // nums 是以“引用”方式传递的。也就是说，不对实参做任何拷贝
> int len = removeDuplicates(nums);
>
> // 在函数里修改输入数组对于调用者是可见的。
> // 根据你的函数返回的长度, 它会打印出数组中 该长度范围内 的所有元素。
> for (int i = 0; i < len; i++) {
> print(nums[i]);
> }
> 示例 1：
> 输入：nums = [1,1,2]
> 输出：2, nums = [1,2]
> 解释：函数应该返回新的长度 2 ，并且原数组 nums 的前两个元素被修改为 1, 2 。不需要考虑数组中超出新长度后面的元素。

```python
class Solution:
    def removeDuplicates(self, nums):
        n = len(nums)
        if n <= 2:
            return

        l, r = 0, 1
        while r < n:
            if nums[l] == nums[r]:
                r += 1
            else:
                l += 1
                nums[l] = nums[r]
        return l + 1
```

#### [27]移除元素

> 给你一个数组 nums 和一个值 val，你需要 原地 移除所有数值等于 val 的元素，并返回移除后数组的新长度。
>
>  不要使用额外的数组空间，你必须仅使用 O(1) 额外空间并 原地 修改输入数组。
> 元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素。
> 说明:
> 为什么返回数值是整数，但输出的答案是数组呢?
> 请注意，输入数组是以「引用」方式传递的，这意味着在函数里修改输入数组对于调用者是可见的。
> 你可以想象内部操作如下:
> // nums 是以“引用”方式传递的。也就是说，不对实参作任何拷贝
> int len = removeElement(nums, val);
> // 在函数里修改输入数组对于调用者是可见的。
> // 根据你的函数返回的长度, 它会打印出数组中 该长度范围内 的所有元素。
> for (int i = 0; i < len; i++) {
> print(nums[i]);
> }
> 示例 1：
> 输入：nums = [3,2,2,3], val = 3
> 输出：2, nums = [2,2]
> 解释：函数应该返回新的长度 2, 并且 nums 中的前两个元素均为 2。你不需要考虑数组中超出新长度后面的元素。例如，函数返回的新长度为
> 2 ，而
> nums = [2,2,3,3] 或 nums = [2,2,0,0]，也会被视作正确答案。

```python
class Solution:
    def removeElement(self, nums, val):
        n = len(nums)
        if n <= 2:
            return

        l, r = 0, 0
        while r < n:
            if nums[r] != val:
                nums[l] = nums[r]
                l += 1
                r += 1
            else:
                r += 1

        return l
```

#### [31]下一个排列

> 实现获取 下一个排列 的函数，算法需要将给定数字序列重新排列成字典序中下一个更大的排列（即，组合出下一个更大的整数）。
> 如果不存在下一个更大的排列，则将数字重新排列成最小的排列（即升序排列）。
> 必须 原地 修改，只允许使用额外常数空间。
> 示例 1：
> 输入：nums = [1,2,3]
> 输出：[1,3,2]

```python
class Solution:
    def nextPermutation2(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.

        标准的“下一个排列”算法可以描述为：
        1. 从后向前查找第一个相邻升序的元素对 (i,j)，满足 A[i] < A[j]。此时 [j,end) 必然是降序
        2. 在 [j,end) 从后向前查找第一个满足 A[i] < A[k] 的 k。A[i]、A[k] 分别就是上文所说的「小数」、「大数」
        将 A[i] 与 A[k] 交换
        3. 可以断定这时 [j,end) 必然是降序，逆置 [j,end)，使其升序
        4. 如果在步骤 1 找不到符合的相邻元素对，说明当前 [begin,end) 为一个降序顺序，则直接跳到步骤 4
        """
        i, j, k = len(nums) - 2, len(nums) - 1, len(nums) - 1

        #  find: A[i] < A[j]
        while i >= 0 and nums[i] >= nums[j]:
            i -= 1
            j -= 1

        if i >= 0:  # 不是最后一个排列,即不是该序列最大的排列组合
            # find: A[i] < A[k]
            while nums[i] >= nums[k]:
                k -= 1
                #  swap A[i], A[k]
            nums[i], nums[k] = nums[k], nums[i]

        #  reverse  A[j:end]
        i, j = j, len(nums) - 1
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i = i + 1
            j = j - 1
```

#### [88]归并两个排序数组

> 给你两个按 非递减顺序 排列的整数数组 nums1 和 nums2，另有两个整数 m 和 n ，分别表示 nums1 和 nums2 中的元素数目。
> 请你 合并 nums2 到 nums1 中，使合并后的数组同样按 非递减顺序 排列。
> 注意：最终，合并后数组不应由函数返回，而是存储在数组 nums1 中。为了应对这种情况，nums1 的初始长度为 m + n，其中前 m 个元素表示应合并
> 的元素，后 n 个元素为 0 ，应忽略。nums2 的长度为 n 。
> 示例 1：
> 输入：nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
> 输出：[1,2,2,3,5,6]
> 解释：需要合并 [1,2,3] 和 [2,5,6] 。
> 合并结果是 [1,2,2,3,5,6] ，其中斜体加粗标注的为 nums1 中的元素。

```python
class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        Do not return anything, modify nums1 in-place instead.
        由于数组已经排好序，因此将指针放在两数组的尾部是关键
        其他的就依次比较，插入到位置就好了
        """
        if m == 0:  # for case: nums1 = [0] m, n = 0, 1, nums2 = [1]
            for i in range(len(nums1)):
                nums1[i] = nums2[i]
        else:
            p1, p2, q = m - 1, n - 1, m + n - 1

            while p1 >= 0 and p2 >= 0:
                if nums1[p1] > nums2[p2]:
                    nums1[q] = nums1[p1]
                    q -= 1
                    p1 -= 1
                else:
                    nums1[q] = nums2[p2]
                    q -= 1
                    p2 -= 1

            while p2 >= 0:
                # for case: nums1 = [2, 0], m, n = 1, 1, nums2 = [1]
                # p2还不等于0，则依次把nums2中的派到nums1中前面
                nums1[p2] = nums2[p2]
                p2 -= 1
```

#### [142]环形链表II (快慢指针）

> 给定一个链表，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。
> 如果链表中有某个节点，可以通过连续跟踪 next 指针再次到达，则链表中存在环。 为了表示给定链表中的环，评测系统内部使用整数
> pos 来表示链表尾连接到
> 链表中的位置（索引从 0 开始）。如果 pos 是 -1，则在该链表中没有环。注意：pos 不作为参数进行传递，仅仅是为了标识链表的实际情况。
> 不允许修改 链表。
> 示例 1：
> 输入：head = [3,2,0,-4], pos = 1
> 输出：返回索引为 1 的链表节点
> 解释：链表中有一个环，其尾部连接到第二个节点。

```python
class Solution(object):
    def detectCycle(self, head):
        '''
        假设 x为 头-环入口 的节点数， y为 环入口-相遇点 的节点数  z为 相遇点-环入口 的节点数
        第一次相遇时：
        slow指针走过的节点数为: x + y,fast指针走过的节点数： x + y + n (y + z)，n为圈数，（y+z）为 一圈内节点的个数
        因为fast指针是一步走两个节点，slow指针一步走一个节点， 所以 fast指针走过的节点数 = slow指针走过的节点数 * 2
        (x + y) * 2 = x + y + n (y + z)
        消掉（x+y）: x + y = n (y + z)
        因为我们要找环形的入口，那么要求的是x，因为x表示 头结点到 环形入口节点的的距离。
        所以我们要求x ，将x单独放在左面：x = n (y + z) - y
        y融合进去，整理公式之后：x = (n - 1) (y + z) + z
        注意这里n一定是大于等于1的，因为 fast指针至少要多走一圈才能相遇slow指针
        1.当 n为1的时候，公式就化解为 x = z
            这就意味着，从头结点出发一个指针，从相遇节点 也出发一个指针，这两个指针每次只走一个节点，
            那么当这两个指针相遇的时候就是 环形入口的节点
            也就是在相遇节点处，定义一个指针index1，在头结点处定一个指针index2。
            让index1和index2同时移动，每次移动一个节点， 那么他们相遇的地方就是 环形入口的节点。
        2.那么n如果大于1是什么情况呢，就是fast指针在环形转n圈之后才遇到 slow指针。
            其实这种情况和n为1的时候 效果是一样的，一样可以通过这个方法找到 环形的入口节点，
            只不过，index1 指针在环里 多转了(n-1)圈，然后再遇到index2，相遇点依然是环形的入口节点。
        '''
        fast, slow = head, head
        while fast and fast.next:
            fast, slow = fast.next.next, slow.next

            if fast == slow:
                fast = head
                while fast != slow:
                    fast, slow = fast.next, slow.next
                return fast
        return None
```

#### [633]平方数之和

> 给定一个非负整数 c ，你要判断是否存在两个整数 a 和 b，使得 a² + b² = c 。
> 示例 1：
> 输入：c = 5
> 输出：true
> 解释：1 * 1 + 2 * 2 = 5

```python
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        # 时间复杂度为 O(sqrt(c)) solution 633 is valuable
        l, r = 0, int(c ** 0.5)
        while l <= r:
            if l ** 2 + r ** 2 < c:
                l += 1
            elif l ** 2 + r ** 2 > c:
                r -= 1
            else:
                return True
        return False

```

#### [680]验证回文字符串II

> 给定一个非空字符串 s，最多删除一个字符。判断是否能成为回文字符串。
> 示例 1:
> 输入: s = "aba"
> 输出: true

```python
class Solution:
    def validPalindrome(self, s: str) -> bool:
        '''
        双指针：头尾指针l,r向中间滑动
            当碰到s[l]!=s[r]时，产生两种情况，移动左指针或移动右指针（即删除左字母或右字母）
            所以会产生两个子串s[l+1:r+1]与s[l:r]，判断两个子串是否为回文子串
        Time:O(N)
        Space:O(N)
        由于判断是否回文使用了 [::-1] 翻转形成了新字符串，所以空间复杂度是O(N)。
        如果不通过翻转的方式来判断，空间复杂度可以降到O(1)
        '''
        isPalindrome = lambda s: s == s[::-1]
        l, r = 0, len(s) - 1

        while l < r:
            if s[l] != s[r]:
                return isPalindrome(s[l + 1:r + 1]) or isPalindrome(s[l:r])
            else:
                l += 1
                r -= 1
        return True
```

#### [524]通过删除字母匹配到字典里最长单词

> 给你一个字符串 s 和一个字符串数组 dictionary ，找出并返回 dictionary 中最长的字符串，该字符串可以通过删除 s 中的某些字符得到。
> 如果答案不止一个，返回长度最长且字母序最小的字符串。如果答案不存在，则返回空字符串。
> 示例 1：
> 输入：s = "abpcplea", dictionary = ["ale","apple","monkey","plea"]
> 输出："apple"

```python
class Solution:
    def findLongestWord(self, s, dictionary):
        '''
        归并两个有序数组的变形题, 思路基本一致。
        '''
        dictionary = sorted(dictionary, key=lambda x: (-len(x), x))

        for word in dictionary:
            p1, p2 = len(word) - 1, len(s) - 1
            while p1 >= 0 and p2 >= 0:
                if word[p1] == s[p2]:
                    p1 -= 1
                    p2 -= 1
                else:
                    p2 -= 1
            if p1 == -1:
                return word
        return ''
```
