# 给定一个长度为4的整数数组 cards 。你有 4 张卡片，每张卡片上都包含一个范围在 [1,9] 的数字。您应该使用运算符 ['+', '-', '*',
#  '/'] 和括号 '(' 和 ')' 将这些卡片上的数字排列成数学表达式，以获得值24。 
# 
#  你须遵守以下规则: 
# 
#  
#  除法运算符 '/' 表示实数除法，而不是整数除法。
# 
#  
#  例如， 4 /(1 - 2 / 3)= 4 /(1 / 3)= 12 。 
#  
#  
#  每个运算都在两个数字之间。特别是，不能使用 “-” 作为一元运算符。
#  
#  例如，如果 cards =[1,1,1,1] ，则表达式 “-1 -1 -1 -1” 是 不允许 的。 
#  
#  
#  你不能把数字串在一起
#  
#  例如，如果 cards =[1,2,1,2] ，则表达式 “12 + 12” 无效。 
#  
#  
#  
# 
#  如果可以得到这样的表达式，其计算结果为 24 ，则返回 true ，否则返回 false 。 
# 
#  
# 
#  示例 1: 
# 
#  
# 输入: cards = [4, 1, 8, 7]
# 输出: true
# 解释: (8-4) * (7-1) = 24
#  
# 
#  示例 2: 
# 
#  
# 输入: cards = [1, 2, 1, 2]
# 输出: false
#  
# 
#  
# 
#  提示: 
# 
#  
#  cards.length == 4 
#  1 <= cards[i] <= 9 
#  
#  Related Topics 数组 数学 回溯 👍 410 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def __init__(self):
        self.add = 0
        self.multiply = 1
        self.subtract = 2
        self.divide = 3
        self.target = 24
        self.epsilon = 1e-6  # 除法运算为实数除法，因此结果为浮点数，列表中存储的数字也都是浮点数。在判断结果是否等于 2424 时应考虑精度误差，这道题中，误差小于 10−610−6 可以认为是相等


    def judgePoint24(self, cards: [int]) -> bool:

        return self.dfs(cards)

    def dfs(self, nums):
        if not nums:
            return False
        if len(nums) == 1:
            return abs(nums[0] - self.target) < self.epsilon

        n = len(nums)
        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                new_nums = []

                for k in range(n):
                    if k != i and k != j:
                        new_nums.append(nums[k])

                a, b = nums[i], nums[j]

                for v in range(4):
                    # 加法和乘法都满足交换律，因此如果选择的运算操作是加法或乘法，则对于选出的2
                    # 个数字不需要考虑不同的顺序，在遇到第二种顺序时可以不进行运算，直接跳过。
                    if v < 2 and i > j:
                        continue
                    if v == self.add:
                        new_nums.append(a + b)
                    if v == self.multiply:
                        new_nums.append(a * b)
                    if v == self.subtract:
                        new_nums.append(a - b)
                    if v == self.divide:
                        if abs(b) < self.epsilon:
                            continue
                        new_nums.append(a / b)

                    if self.dfs(new_nums):
                        return True
                    new_nums.pop()
        return False


class Solution2:
    def judgePoint24(self, nums: [int]) -> bool:
        TARGET = 24
        EPSILON = 1e-6
        ADD, MULTIPLY, SUBTRACT, DIVIDE = 0, 1, 2, 3

        def solve(nums: [float]) -> bool:
            if not nums:
                return False
            if len(nums) == 1:
                return abs(nums[0] - TARGET) < EPSILON
            for i, x in enumerate(nums):
                for j, y in enumerate(nums):
                    if i != j:
                        newNums = list()
                        for k, z in enumerate(nums):
                            if k != i and k != j:
                                newNums.append(z)
                        for k in range(4):
                            if k < 2 and i > j:
                                continue
                            if k == ADD:
                                newNums.append(x + y)
                            elif k == MULTIPLY:
                                newNums.append(x * y)
                            elif k == SUBTRACT:
                                newNums.append(x - y)
                            elif k == DIVIDE:
                                if abs(y) < EPSILON:
                                    continue
                                newNums.append(x / y)
                            if solve(newNums):
                                return True
                            newNums.pop()
            return False

        return solve(nums)


# leetcode submit region end(Prohibit modification and deletion)

if __name__ == "__main__":
    # nums = [4, 1, 8, 7]
    nums = [1, 2, 1, 2]
    S = Solution()
    print(S.judgePoint24(nums))
