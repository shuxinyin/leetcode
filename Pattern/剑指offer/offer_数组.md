## 数组

[剑指 Offer 03]数组中重复的数字
[剑指 Offer 53 - I]在排序数组中查找数字 I
[剑指 Offer 53 - II]0～n-1中缺失的数字

[剑指 Offer 14- I]剪绳子
[剑指 Offer 14- II]剪绳子 II

[剑指 Offer 57]和为s的两个数字
[剑指 Offer 57 - II]和为s的连续正数序列

[剑指 Offer 62]圆圈中最后剩下的数字.py
[剑指 Offer 66]构建乘积数组.py
[剑指 Offer 39]数组中出现次数超过一半的数字


#### [剑指 Offer 03]找出数组中重复的数字。 
> 在一个长度为 n 的数组 nums 里的所有数字都在 0～n-1 的范围内。数组中某些数字是重复的，但不知道有几个数字重复了，也不知道每个数字重复了几次。请
> 找出数组中任意一个重复的数字。 
>  示例 1： 
>  输入：
> [2, 3, 1, 0, 2, 5, 3]
> 输出：2 或 3 

```python
class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        res = set()

        for n in nums:
            if n in res:
                return n
            else:
                res.add(n)
```

#### [剑指 Offer 53 - I]在排序数组中查找数字 I
> 统计一个数字在排序数组中出现的次数。 
> 输入: nums = [5,7,7,8,8,10], target = 8
> 输出: 2 

>  示例 2: 
> 输入: nums = [5,7,7,8,8,10], target = 6
> 输出: 0 

```python
class Solution:
    def search(self, nums: [int], target: int) -> int:

        def helper(target):
            l, r = 0, len(nums)-1

            while l <= r:
                mid = l + (r - l) // 2
                if nums[mid] <= target:
                    l = mid + 1
                else:
                    r = mid - 1
            return l  # i永远是大于target的下一个数

        return helper(target) - helper(target - 1)

```


#### [剑指 Offer 53 - II]0～n-1中缺失的数字

> 一个长度为n-1的递增排序数组中的所有数字都是唯一的，并且每个数字都在范围0～n-1之内。
> 在范围0～n-1内的n个数字中有且只有一个数字不在该数组中，请找出这个数字。
>  示例 1:  
>  输入: [0,1,3]
> 输出: 2

>  示例 2: 
>  输入: [0,1,2,3,4,5,6,7,9]
>  输出: 8 

```python
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        def helper():
            l, r = 0, len(nums)-1

            while l <= r:
                mid = l + (r - l) // 2
                if nums[mid] == mid:
                    l = mid + 1
                else:
                    r = mid - 1
            return l  # i永远是大于target的下一个数

        return helper(nums)
```

#### [剑指 Offer 14- I]剪绳子

Q: 给你一根长度为 n 的绳子，请把绳子剪成整数长度的 m 段（m、n都是整数，n>1并且m>1），每段绳子的长度记为 k[0],k[1]...k[m-1] 。
请问 k[0]* k[1] *...* k[m-1] 可能的最大乘积是多少？ 例如，当绳子的长度是8时，我们把它剪成长度分别为2、3、3的三段，此时得到的最大乘积是18

```python
class Solution:
    # Method1: math solution. 
    def cuttingRope(self, n: int) -> int:
        # wait to test.
        if n < 4:
            return n - 1
        res = 1
        while n > 4:
            res = res * 3
            n -= 3
        return res * n

    def cuttingRope(self, n: int) -> int:
        '''
        a+b+...+c >= n * sqrt(ab*...*c), 当且仅当 a==b=...=c 等号成立
        '''

        import math
        if n <= 3:
            return n - 1
        a, b = n // 3, n % 3

        if b == 0:
            return int(math.power(3, a))
        if b == 1:
            return int(math.power(3, a - 1)) * 4
        return int(math.power(3, a)) * 2

    # Method2: dp solution. 
    def cuttingRope(self, n: int) -> int:
        '''
        状态：dp[i]表示长度为i的绳子的最大乘积
        2.状态转移:dp[i]分两种情况 乘积为2个， 乘积为3个 。
            2.1 由前面某一个dp[j]*(i-j)得到,即前面剪了>=2段,后面再剪一段,此时的乘积个数>=3个
            2.2 前面单独成一段,后面剩下的单独成一段,乘积为j*(i-j),乘积个数为2
            两种情况中取大的值作为dp[i]的值,同时应该遍历所有j,j∈[1,i-1],取最大值
        3.初始化:初始化dp[1]=1即可
        '''
        dp = [1 for i in range(n + 1)]

        for i in range(2, n + 1):
            for j in range(1, i):
                tmp = max(j * (i - j), dp[j] * (i - j))
                dp[i] = max(tmp, dp[i])
        return dp[-1]
```

#### [剑指 Offer 14- II]剪绳子 II

Q: 给你一根长度为 n 的绳子，请把绳子剪成整数长度的 m 段（m、n都是整数，n>1并且m>1），每段绳子的长度记为 k[0],k[1]...k[m - 1] 。
请问 k[0]*k[1]*...*k[m - 1] 可能的最大乘积是多少？例如，当绳子的长度是8时，我们把它剪成长度分别为2、3、3的三段，此时得到的最大乘积是18。
> 答案需要取模 1e9+7（1000000007），如计算初始结果为：1000000008，请返回 1。

```python
class Solution:
    def cuttingRope(self, n: int) -> int:
        # 如果n == 2，返回1
        # 如果n == 3，返回2，两个可以合并成n小于4的时候返回n - 1
        # 如果n == 4，返回4
        # 如果n > 4，分成尽可能多的长度为3的小段，每次循环长度n减去3，乘积res乘以3；最后返回时乘以小于等于4的最后一小段；
        # 每次乘法操作后记得取余就行以上2和3可以合并

        if n < 4:
            return n - 1
        res = 1
        while n > 4:
            res = res * 3 % 1000000007
            n -= 3
        return res * n % 1000000007

```

#### [剑指 Offer 57]和为s的两个数字

>  输入一个递增排序的数组和一个数字s，在数组中查找两个数，使得它们的和正好是s。如果有多对数字的和等于s，则输出任意一对即可。 
>  示例 1： 
>  输入：nums = [2,7,11,15], target = 9
>  输出：[2,7] 或者 [7,2]

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        n = len(nums)
        for i in range(n):
            if nums[i] not in dic:
                dic[target-nums[i]] = nums[i]
            else:
                return [nums[i], target-nums[i]]
        return -1
```



#### [剑指 Offer 57 - II]和为s的连续正数序列

Q: 输入一个正整数 target ，输出所有和为 target 的**连续正整数序列**（至少含有两个数）。
序列内的数字由小到大排列，不同序列按照首个数字从小到大排列。


> 输入：target = 15
> 输出：[[1,2,3,4,5],[4,5,6],[7,8]]

```python
class Solution:
    def findContinuousSequence(self, target: int) -> List[List[int]]:
        ''' DFS
        '''
        nums = [i for i in range(target)]
        res = []

        def dfs(path, target):
            if target == 0:
                res.append(list(path))
            if target < 0:
                return

            for i in range(len(nums)):
                dfs(path + nums[i], target - nums[i])

        return res

    def findContinuousSequence(self, target: int) -> List[List[int]]:
        # Double pointer
        # Time: O(N),N=len(target)
        # Space: O(1)
        i, j, s, res = 1, 2, 3, []
        while i < j:
            if s == target:
                res.append(list(range(i, j + 1)))
            if s >= target:
                s -= i
                i += 1
            else:
                j += 1
                s += j
        return res
```

#### [剑指 Offer 62]圆圈中最后剩下的数字

> 0,1,···,n-1这n个数字排成一个圆圈，从数字0开始，每次从这个圆圈里删除第m个数字（删除后从下一个数字开始计数）。求出这个圆圈里剩下的最后一个数字。
> 例如，0、1、2、3、4这5个数字组成一个圆圈，从数字0开始每次删除第3个数字，则删除的前4个数字依次是2、0、4、1，因此最后剩下的数字是3。

```python
class Solution:
    def lastRemaining(self, n: int, m: int) -> int:
        nums = [i for i in range(n)]

        def dfs(nums, cur_ind):
            if len(nums) == 1:
                return

            pip_index = (cur_ind + m) % len(nums)
            nums.pop(pip_index)

            dfs(nums, pip_index)

        dfs(nums, m)

        return nums[0]

    def lastRemaining(self, n: int, m: int) -> int:
        # 假设m=3, 最后剩下的那个数为x，下标为0. [3]
        # 倒数第二轮，剩下2个数， 此时x位置下标为（0+3）%2=1. [1, 3， 1， 3]
        # 倒数第三轮，剩下3个数， 此时x位置下标为（1+3）%3=1. [1, 3, 4， 1， 3， 4]
        # 倒数第四轮，剩下4个数， 此时x位置下标为（1+3）%4=0. [3，4， 0, 1, 3, 4， 0， 1]
        # 倒数第五轮，剩下5个数， 此时x位置下标为（0+3）%5=3. [0, 1, 2, 3, 4， 0， 1， 2， 3， 4]
        # 以此倒推就得(当前index + m) % 上一轮剩余数字的个数

        ans = 0
        # 最后一轮剩下2人，所有从2开始反推。
        for i in range(2, n + 1):
            ans = (ans + m) % i
        return ans
```



#### [剑指 Offer 66]构建乘积数组

Q: 给定一个数组 A[0,1,…,n-1]，请构建一个数组 B[0,1,…,n-1]，其中 B[i] 的值是数组 A 中除了下标 i 以外的元素的积,
即 B[i]=A[0]×A[1]×…×A[i-1]×A[i+1]×…×A[n-1]。不能使用除法。

> 输入: [1,2,3,4,5]
> 输出: [120,60,40,30,24]

```python
class Solution:
    def constructArr(self, a: List[int]) -> List[int]:
        ''' 本质上： 是计算 除对角线外的所有数 的 乘积 = 下三角 * 上三角
            [1,2,3,4,5]
            [1,1,3,4,5]
            [1,2,1,4,5]
            [1,2,3,1,5]
            [1,2,3,4,1]
        '''
        n = len(a)
        b = [1] * n  # b为下三角
        c = [1] * n  # c为上三角
        for i in range(1, n):
            b[i] = b[i - 1] * a[i - 1]  # b此时为下三角

        for i in range(n - 2, -1, -1):
            c[i] = c[i + 1] * a[i + 1]
            # b[i] *= tmp
        res = [c[i] * b[i] for i in range(n)]
        return res
```

#### [剑指 Offer 39]数组中出现次数超过一半的数字
Q:  数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。
你可以假设数组是非空的，并且给定的数组总是存在多数元素。

> 输入: [1, 2, 3, 2, 2, 2, 5, 4, 2]
> 输出: 2

```python
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ''' 采用投票、抵消策略， 相同数字 +1 不同则-1， 则最后剩下的为众数
        '''
        votes = 0
        for n in nums:
            # 票数为0, 重设众数
            if votes == 0:
                x = n

            if n == x:
                votes += 1
            else:
                votes -= 1
        return x
```