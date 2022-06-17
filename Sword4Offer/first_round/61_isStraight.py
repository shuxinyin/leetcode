class Solution:
    def isStraight(self, nums: List[int]) -> bool:
        '''
        满足以下两点条件的都是符合要求的
        1.除大小王外，所有牌无重复
        2.设此5张牌中最大的牌为max ，最小的牌为min（大小王除外），max-mid<5
        '''
        repeat = set()

        for n in nums:
            if n == 0:
                continue
            if n in repeat:
                return False
            repeat.add(n)
        max_value, min_value = max(repeat), min(repeat)

        return max_value - min_value < 5
