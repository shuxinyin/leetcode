class Solution:
    def translateNum(self, num: int) -> int:
        '''
        # Time: O(N), Space: O(N)
        # 这个题类似于小跳蛙爬楼梯。
        状态定义：列表dp， dp[i]表示xi为结尾的数字翻译方案数量
        转移方程：若x_i与x_i-1组成的两位数字可以被翻译，则dp[i]=dp[i-1]+dp[i-2]
                否则x_i与x_i-1组成的两位数字不可以被翻译：dp[i]=dp[i-1]
        初始状态： dp[0]=nums[0], 以nums[0]为结尾的子数组的最大连续子数组最大和nums[0]
        返回值： 返回dp[row][col]，代表最大值
        '''
        s = str(num)
        a = b = 1
        for i in range(2, len(s) + 1):
            tmp = s[i - 2:i]
            c = a + b if "10" <= tmp <= "25" else a

            b = a
            a = c
        return a
