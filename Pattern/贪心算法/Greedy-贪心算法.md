## 贪心算法

455. 分配饼干
135. 发糖果

435. 无重叠区间
452. 用最少数量的箭引爆气球
56. 合并区间

605. 种花
763. 划分字母区间
406. 根据身高重建队列
665. 非递减数列



#### 455. 分配饼干

Q: 假设你是一位很棒的家长，想要给你的孩子们一些小饼干。但是，每个孩子最多只能给一块饼干。
对每个孩子 i，都有一个胃口值 g[i]，这是能让孩子们满足胃口的饼干的最小尺寸；并且每块饼干 j，都有一个尺寸 s[j] 。
如果 s[j] >= g[i]，我们可以将这个饼干 j 分配给孩子 i ，这个孩子会得到满足。你的目标是尽可能满足越多数量的孩子，并输出这个最大数值。


> 输入: g = [1,2], s = [1,2,3]  
> 输出: 2  
> 解释:   
> 你有两个孩子和三块小饼干，2个孩子的胃口值分别是1,2。  
> 你拥有的饼干数量和尺寸都足以让所有孩子满足。  
> 所以你应该输出2.

```python
class Solution:
    def findContentChildren(self, g, s) -> int:
        '''
        贪心思想： 从胃口最小的小孩子满足起，分配最小且能满足胃口的饼干，则每一步都是最好的安排
        解题思路：
            此处不要第一想法想着用for循环。
            采用两个index，ind1标记g,ind2标记s
            while 做一个判断循环即可

        时间复杂度： 排序O(nlogn) + n
        '''

        g.sort()
        s.sort()

        ind1, ind2, res = 0, 0, 0
        while ind1 < len(g) and ind2 < len(s):
            if g[ind1] <= s[ind2]:
                res += 1
                ind1 += 1
                ind2 += 1
            else:
                ind2 += 1

        return res
```

#### 135. 发糖果

> Q: 老师想给孩子们分发糖果，有 N 个孩子站成了一条直线，老师会根据每个孩子的表现，预先给他们评分。
> 你需要按照以下要求，帮助老师给这些孩子分发糖果：
> 每个孩子至少分配到 1 个糖果。
> 评分更高的孩子必须比他两侧的邻位孩子获得更多的糖果。
> 那么这样下来，老师至少需要准备多少颗糖果呢？

> 示例 1：
> 输入：[1,0,2]
> 输出：5
> 解释：你可以分别给这三个孩子分发 2、1、2 颗糖果。

```python
class Solution:
    def candy(self, ratings) -> int:
        '''
        规则定义： 设学生 A 和学生 B 左右相邻，A 在 B 左边；
        左规则： 当 ratingsB>ratingsA时，B 的糖比 A 的糖数量多。
        右规则： 当 ratingsA>ratingsB时，A 的糖比 B 的糖数量多。
        相邻的学生中，评分高的学生必须获得更多的糖果 等价于 所有学生满足左规则且满足右规则。

        解决方法： 遍历两遍，
                第一遍：从左至右边遍历，满足左规则, 结果存于left_list
                第二遍：从右往左遍历， 满足右规则, 结果存于right_list
                遍历： count += max(left, right)
        时间 O(N), 空间O（N）
        '''
        n = len(ratings)

        left_list = [1] * n
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                left_list[i] = left_list[i - 1] + 1

        count = left_list[-1]  # 由于right_candy[-1]=1, left_candy[-1]必大于由于right_candy[-1]

        right_list = [1] * n
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                right_list[i] = right_list[i + 1] + 1
            count += max(left_list[i], right_list[i])

        return count
```

#### 435. 无重叠区间

> 给定一个区间的集合，找到需要移除区间的最小数量，使剩余区间互不重叠。
> 注意:
> 可以认为区间的终点总是大于它的起点。
> 区间 [1,2] 和 [2,3] 的边界相互“接触”，但没有相互重叠。
>
> 示例 1:
> 输入: [[1,2], [2,3], [3,4], [1,3]]
> 输出: 1
> 解释: 移除 [1,3] 后，剩下的区间没有重叠。

```python
class Solution:
    def eraseOverlapIntervals(self, intervals) -> int:
        ''' 有重叠， gap最大的， delete
        '''
        intervals = sorted(intervals, key=lambda x: x[0])

        n = len(intervals)
        count = 0
        end = intervals[0][1]
        for i in range(1, n):
            #  下一个区间 head < 尾 有重叠
            if intervals[i][0] < end:
                count += 1
                end = min(intervals[i][1], end)
            else:
                end = intervals[i][1]
        return count
```

#### 452. 用最少数量的箭引爆气球

> 在二维空间中有许多球形的气球。对于每个气球，提供的输入是水平方向上，气球直径的开始和结束坐标。
> 由于它是水平的，所以纵坐标并不重要，因此只要知道开始和结束的横坐标就足够了。开始坐标总是小于结束坐标。
> 一支弓箭可以沿着 x 轴从不同点完全垂直地射出。在坐标 x 处射出一支箭，若有一个气球的直径的开始和结束坐标为 xstart，xend，
> 且满足
> xstart ≤ x ≤ xend，则该气球会被引爆。可以射出的弓箭的数量没有限制。 弓箭一旦被射出之后，可以无限地前进。我们想找到使得所有气球全部被引爆，所需的弓箭的
> 最小数量。
> 给你一个数组 points ，其中 points [i] = [xstart,xend] ，返回引爆所有气球所必须射出的最小弓箭数。

> 示例 1：
> 输入：points = [[10,16],[2,8],[1,6],[7,12]]
> 输出：2
> 解释：对于该样例，x = 6 可以射爆 [2,8],[1,6] 两个气球，以及 x = 11 射爆另外两个气球

```python
class Solution:
    def findMinArrowShots(self, intervals) -> int:
        ''' 
        '''
        intervals = sorted(intervals, key=lambda x: x[0])

        n = len(intervals)
        count = 0
        end = intervals[0][1]
        for i in range(1, n):
            # 有重叠
            if intervals[i][0] <= end:
                end = min(intervals[i][1], end)
            else:
                count += 1
                end = max(intervals[i][1], end)
        return count

    def findMinArrowShots2(self, intervals) -> int:
        '''
        same with question 435 but something different
        different: 1.右排序
        首先要对区间进行排序，这里先以区间的尾来排序（右排序），然后在遍历区间。
        1，箭从第一个区间尾射出，如果后面区间的头小于等于当前区间的尾
        比如当前区间是[4,5]，后面区间是[3,6]或者是[5,9]
        说明这两个区间有重复，则箭可以贯穿，
        2，如果后面区间的头大于当前区间的尾，说明他们没有重合，箭+1，从这个区间尾射出
        Time: O(Nlog N)
        Space: O(1)
        '''
        intervals = sorted(intervals, key=lambda x: x[1])

        end = intervals[0][1]  # 记录区间尾部的位置
        count = 1
        for i in range(1, len(intervals)):
            if intervals[i][0] <= end:
                continue
            else:
                # 如果没有重叠，就不需要移除，只需要更新尾部的位置即可
                end = intervals[i][1]
                count += 1

        return count
```
#### 56. 合并区间

> 以数组 intervals 表示若干个区间的集合，其中单个区间为 intervals[i] = [starti, endi] 。
> 请你合并所有重叠的区间，并返回 一个不重叠的区间数组，该数组需恰好覆盖输入中的所有区间 。
>  示例 1： 
> 输入：intervals = [[1,3],[2,6],[8,10],[15,18]]
> 输出：[[1,6],[8,10],[15,18]]
> 解释：区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].

```python
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda x: x[0])

        merge = []
        for inter in intervals:
            if not merge or merge[-1][1] < inter[0]:
                merge.append(inter)
            else:
                merge[-1][1] = max(merge[-1][1], inter[1])  # 存在[(1, 3), (1, 2)]
        return merge
```
#### 605. 种花

> 假设有一个很长的花坛，一部分地块种植了花，另一部分却没有。可是，花不能种植在相邻的地块上，它们会争夺水源，两者都会死去。
> 给你一个整数数组 flowerbed 表示花坛，由若干 0 和 1 组成，其中 0 表示没种植花，1 表示种植了花。另有一个数 n ，能否在不打破种植规则
> 的情况下种入 n 朵花？能则返回 true ，不能则返回 false。

> 示例 1：
> 输入：flowerbed = [1,0,0,0,1], n = 1
> 输出：true

```python
class Solution:
    def canPlaceFlowers(self, flowerbed, n) -> bool:
        '''首先采用一次跳两格方法
            规律：在初始给的flowerbed数组中， 若当前格子i为1， 则下个格子必为0（因为不能相邻）
            其次， 若当前格子i为0，若当前i = n-1, 或者i的下个格子不是1，果断种花填充。
        '''
        length = len(flowerbed)
        i = 0
        while i < length:
            if flowerbed[i] == 0:
                if i == length - 1 or flowerbed[i + 1] == 0:
                    n -= 1
                else:
                    i += 1
            i += 2  # 是1就跳两格

        return n <= 0     
```

#### 763. 划分字母区间

> 字符串 S 由小写字母组成。我们要把这个字符串划分为尽可能多的片段，同一字母最多出现在一个片段中。返回一个表示每个字符串片段的长度的列表。
> 示例：
> 输入：S = "ababcbacadefegdehijhklij"
> 输出：[9,7,8]
> 解释：
> 划分结果为 "ababcbaca", "defegde", "hijhklij"。
> 每个字母最多出现在一个片段中。
> 像 "ababcbacadefegde", "hijhklij" 的划分是错误的，因为划分的片段数较少。

```python
class Solution:
    def partitionLabels(self, S):
        '''
        1， 首先看第一个字母，找到它在串里最后的一个位置，记作last或一段的最后位置。
        2， 在从0~last这个范围里，挨个查其他字母，看他们的最后位置是不是比刚才的last或这一段的最后位置大。
        如果没有刚才的last或一段的最后位置大，无视它继续往后找。
        如果比刚才的大，说明这一段的分隔位置必须往后移动，所以我们把last或这一段的最后位置更新为当前的字母的最后位置。
        3，肯定到有一个时间（即左边搜索的index==last_index），这个last就更新不了了，那么这个时候这个位置就是我们的分隔位置。
        注意题目要分隔后的长度，我们就用last - startindex + 1。
        4，找到一个分割位，更新一下起始位置，同理搜索就行了。
        '''
        dic = {s: index for index, s in enumerate(S)}  # 存储某个字母对应地最后一个序号
        num = 0  # 直接计数
        result = []
        j = dic[S[0]]  # 第一个字符的最后位置

        for i in range(len(S)):  # 逐个遍历
            num += 1  # 找到一个就加1个长度
            if dic[S[i]] > j:  # 思路一样，如果最后位置比刚才的大，就更新最后位置
                j = dic[S[i]]
            if i == j:  # 思路一样，形式不同，这里就是找到这一段的结束了，就说明当前位置的index和这个字母在字典里的最后位置应该是相同的。
                result.append(num)  # 加入result
                num = 0  # 归0
        return result
```

#### 406. 根据身高重建队列

> 假设有打乱顺序的一群人站成一个队列，数组 people 表示队列中一些人的属性（不一定按顺序）。每个 people[i] = [hi, ki] 表示第 i
> 个人的身高为 hi ，前面 正好 有 ki 个身高大于或等于 hi 的人。
>
>  请你重新构造并返回输入数组 people 所表示的队列。返回的队列应该格式化为数组 queue ，其中 queue[j] = [hj, kj] 是队列中第
> j 个人的属性（queue[0] 是排在队列前面的人）。
>
>  示例 1：
> 输入：people = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]
> 输出：[[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]]
> 解释：
> 编号为 0 的人身高为 5 ，没有身高更高或者相同的人排在他前面。
> 编号为 1 的人身高为 7 ，没有身高更高或者相同的人排在他前面。
> 编号为 2 的人身高为 5 ，有 2 个身高更高或者相同的人排在他前面，即编号为 0 和 1 的人。
> 编号为 3 的人身高为 6 ，有 1 个身高更高或者相同的人排在他前面，即编号为 1 的人。
> 编号为 4 的人身高为 4 ，有 4 个身高更高或者相同的人排在他前面，即编号为 0、1、2、3 的人。
> 编号为 5 的人身高为 7 ，有 1 个身高更高或者相同的人排在他前面，即编号为 1 的人。
> 因此 [[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]] 是重新构造后的队列。

```python
class Solution:
    def reconstructQueue(self, people):
        '''
        规则： 先按照身高h降序排序(身高相同则按K值升序)，然后再重新按照k值插入
        Time: O(N)
        Space: O(1)
        '''

        people = sorted(people, key=lambda x: (-x[0], x[1]))
        #  排序后： [[7, 0], [7, 1], [6, 1], [5, 0], [5, 2], [4, 4]]

        result = []
        for l in people:
            if len(result) < l[1]:
                result.append(l)
            else:
                result.insert(l[1], l)
        #  输出：[[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]]
        return result

```

#### 665. 非递减数列

> 给你一个长度为 n 的整数数组，请你判断在 最多 改变 1 个元素的情况下，该数组能否变成一个非递减数列。
> 我们是这样定义一个非递减数列的： 对于数组中任意的 i (0 <= i <= n-2)，总满足 nums[i] <= nums[i + 1]。
>
> 示例 1:
> 输入: nums = [4,2,3]
> 输出: true
> 解释: 你可以通过把第一个4变成1来使得它成为一个非递减数列。

```python
class Solution(object):
    def checkPossibility(self, nums):
        """
        当 nums[i] 破坏了数组的单调递增时，即 nums[i] < nums[i - 1] 时，为了让数组有序，我们发现一个规律（在上面三个例子中， nums[i] 都为 2， nums[i -1] 都为 4）：
        nums[i]< nums[i-1] 动前不动后
            如例【4，2，5】的情况，当 i = 1 ，那么修改 num[i- 1] ，不要动 nums[i] ，因为nums[i]后面的元素是啥我们还不知道呢，少动它为妙。
            如例【1，4，2，5】的情况，当 i > 1 时，我们应该优先考虑把 nums[i - 1] 调小到 >= nums[i - 2] 并且 <= nums[i]。同样尽量不去修改 nums[i] ，理由同上。
            如例【3，4，2，5】的情况，当 i > 1 且 nums[i] < nums[i - 2] 时，我们无法调整 nums[i - 1] ，我们只能调整 nums[i] 到 nums[i - 1] 。
        Time O(N)
        Space O(1)
        """
        n = len(nums)
        count = 0
        for i in range(1, n):
            if nums[i]< nums[i-1]:
                count += 1
                if i==1 or nums[i] >= nums[i-2]:
                    nums[i-1] = nums[i]
                else:
                    nums[i] = nums[i-1]
        return count <= 1      
```