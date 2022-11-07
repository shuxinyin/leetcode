# 从若干副扑克牌中随机抽 5 张牌，判断是不是一个顺子，即这5张牌是不是连续的。2～10为数字本身，
# A为1，J为11，Q为12，K为13，而大、小王为 0 ，可以看成任意数字。A 不能视为 14。
# 
#  
# 
#  示例 1: 
# 
#  
# 输入: [1,2,3,4,5]
# 输出: True 
# 
#  
# 
#  示例 2: 
# 
#  
# 输入: [0,0,1,2,5]
# 输出: True 
# 
#  
# 
#  限制： 
# 
#  数组长度为 5 
# 
#  数组的数取值为 [0, 13] . 
#  Related Topics 数组 排序 👍 251 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def isStraight(self, nums: List[int]) -> bool:
        '''
        满足以下两点，则都是符合要求的
        1. 除去大小王外， 无重复的牌
        2. max(nums) - min(nums) < 5,（大小王除外）
        '''

        repeat = set()
        for n in nums:
            if n == 0:
                continue
            if n in repeat:
                return False
            repeat.add(n)

        return max(repeat) - min(repeat) < 5
# leetcode submit region end(Prohibit modification and deletion)
