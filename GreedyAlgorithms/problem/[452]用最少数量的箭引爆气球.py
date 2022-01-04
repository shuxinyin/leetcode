# 在二维空间中有许多球形的气球。对于每个气球，提供的输入是水平方向上，气球直径的开始和结束坐标。
# 由于它是水平的，所以纵坐标并不重要，因此只要知道开始和结束的横坐标就足够了。开始坐标总是小于结束坐标。
# 
#  一支弓箭可以沿着 x 轴从不同点完全垂直地射出。在坐标 x 处射出一支箭，若有一个气球的直径的开始和结束坐标为 xstart，xend， 且满足 
# xstart ≤ x ≤ xend，则该气球会被引爆。可以射出的弓箭的数量没有限制。 弓箭一旦被射出之后，可以无限地前进。我们想找到使得所有气球全部被引爆，所需的弓箭的
# 最小数量。 
# 
#  给你一个数组 points ，其中 points [i] = [xstart,xend] ，返回引爆所有气球所必须射出的最小弓箭数。 
#  
# 
#  示例 1： 
# 
#  
# 输入：points = [[10,16],[2,8],[1,6],[7,12]]
# 输出：2
# 解释：对于该样例，x = 6 可以射爆 [2,8],[1,6] 两个气球，以及 x = 11 射爆另外两个气球 
# 
#  示例 2： 
# 
#  
# 输入：points = [[1,2],[3,4],[5,6],[7,8]]
# 输出：4
#  
# 
#  示例 3： 
# 
#  
# 输入：points = [[1,2],[2,3],[3,4],[4,5]]
# 输出：2
#  
# 
#  示例 4： 
# 
#  
# 输入：points = [[1,2]]
# 输出：1
#  
# 
#  示例 5： 
# 
#  
# 输入：points = [[2,3],[2,3]]
# 输出：1
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= points.length <= 10⁴ 
#  points[i].length == 2 
#  -2³¹ <= xstart < xend <= 2³¹ - 1 
#  
#  Related Topics 贪心 数组 排序 👍 495 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findMinArrowShots(self, intervals) -> int:
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
                # 如果重叠了，必须要移除一个，所以count要加1，
                # 然后更新尾部的位置，我们取尾部比较小的
                continue
            else:
                # 如果没有重叠，就不需要移除，只需要更新尾部的位置即可
                end = intervals[i][1]
                count += 1

        return count
# leetcode submit region end(Prohibit modification and deletion)
