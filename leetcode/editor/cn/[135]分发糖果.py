# 老师想给孩子们分发糖果，有 N 个孩子站成了一条直线，老师会根据每个孩子的表现，预先给他们评分。 
# 
#  你需要按照以下要求，帮助老师给这些孩子分发糖果： 
# 
#  
#  每个孩子至少分配到 1 个糖果。 
#  评分更高的孩子必须比他两侧的邻位孩子获得更多的糖果。 
#  
# 
#  那么这样下来，老师至少需要准备多少颗糖果呢？ 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：[1,0,2]
# 输出：5
# 解释：你可以分别给这三个孩子分发 2、1、2 颗糖果。
#  
# 
#  示例 2： 
# 
#  
# 输入：[1,2,2]
# 输出：4
# 解释：你可以分别给这三个孩子分发 1、2、1 颗糖果。
#      第三个孩子只得到 1 颗糖果，这已满足上述两个条件。 
#  Related Topics 贪心 数组 👍 722 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
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
        left_candy = [1 for _ in range(len(ratings))]
        right_candy = [1 for _ in range(len(ratings))]
        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i - 1]:
                left_candy[i] = left_candy[i - 1] + 1

        count = left_candy[-1]  # 由于right_candy[-1]=1, left_candy[-1]必大于由于right_candy[-1]
        for j in range(len(ratings) - 2, -1, -1):
            if ratings[j] > ratings[j + 1]:
                right_candy[j] = right_candy[j + 1] + 1

            count += max(left_candy[j], right_candy[j])

        return count
# leetcode submit region end(Prohibit modification and deletion)

# 优化空间 时间 O(N), 空间O（1）
class Solution2:
    def candy(self, ratings) -> int:
        n = len(ratings)
        if n == 0: return 0
        candy_nums = [1] * n

        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                candy_nums[i] = candy_nums[i - 1] + 1

        for i in range(n - 1, 0, -1):
            if ratings[i - 1] > ratings[i]:
                candy_nums[i - 1] = max(candy_nums[i - 1], candy_nums[i] + 1)
        return sum(candy_nums)

if __name__ == "__main__":
    print("s")
    for i in range(4, -1, -1):
        print(i)
