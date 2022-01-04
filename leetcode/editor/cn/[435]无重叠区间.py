# 给定一个区间的集合，找到需要移除区间的最小数量，使剩余区间互不重叠。 
# 
#  注意: 
# 
#  
#  可以认为区间的终点总是大于它的起点。 
#  区间 [1,2] 和 [2,3] 的边界相互“接触”，但没有相互重叠。 
#  
# 
#  示例 1: 
# 
#  
# 输入: [ [1,2], [2,3], [3,4], [1,3] ]
# 
# 输出: 1
# 
# 解释: 移除 [1,3] 后，剩下的区间没有重叠。
#  
# 
#  示例 2: 
# 
#  
# 输入: [ [1,2], [1,2], [1,2] ]
# 
# 输出: 2
# 
# 解释: 你需要移除两个 [1,2] 来使剩下的区间没有重叠。
#  
# 
#  示例 3: 
# 
#  
# 输入: [ [1,2], [2,3] ]
# 
# 输出: 0
# 
# 解释: 你不需要移除任何区间，因为它们已经是无重叠的了。
#  
#  Related Topics 贪心 数组 动态规划 排序 👍 565 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def eraseOverlapIntervals(self, intervals) -> int:
        '''
        首先要对区间进行排序，这里先以区间的头来排序，然后在遍历区间。
        1，如果后面区间的头小于当前区间的尾，
        比如当前区间是[3,6]，后面区间是[4,5]或者是[5,9]
        说明这两个区间有重复，必须要移除一个，那么要移除哪个呢?
        为了防止在下一个区间和现有区间有重叠，我们应该让现有区间越短越好，所以应该移除尾部比较大的，保留尾部比较小的。(故移除[3,6],[5,9])
        2，如果后面区间的头不小于当前区间的尾，说明他们没有重合，不需要移除
        Time: O(NlogN)
        Space: O(1)

        '''
        intervals = sorted(intervals, key=lambda x: x[0])

        end = intervals[0][1]  # 记录区间尾部的位置
        count = 0
        for i in range(1, len(intervals)):
            if intervals[i][0] < end:
                # 如果重叠了，必须要移除一个，所以count要加1，
                # 然后更新尾部的位置，我们取尾部比较小的
                end = min(end, intervals[i][1])
                count += 1
            else:
                # 如果没有重叠，就不需要移除，只需要更新尾部的位置即可
                end = intervals[i][1]
        return count


# leetcode submit region end(Prohibit modification and deletion)


if __name__ == "__main__":
    l = [[1, 2], [2, 4], [1, 3]]
    l2 = sorted(l, key=lambda x: x[0])
    print(l)
    print(l2)
