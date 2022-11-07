## 位运算

[剑指 Offer 15]二进制中1的个数
[剑指 Offer 65]不用加减乘除做加法
[剑指 Offer 56 - I]数组中数字出现的次数
[剑指 Offer 56 - II]数组中数字出现的次数 II


### 异或运算

> 与&：有0为0  
> 或|: 有1为1  
> 非~：换位取反
> 异或^: 相同为0， 不同为1


> 异或运算：x ^ 0 = x​ ， x ^ 1 = ~x
> 与运算：x & 0 = 0 ， x & 1 = x

#### [剑指 Offer 15]二进制中1的个数

Q: 编写一个函数，输入是一个无符号整数（以二进制串的形式），返回其二进制表达式中数字位数为 '1' 的个数（也被称为 汉明重量).）。

```python
class Solution:
    def hammingWeight(self, n: int) -> int:
        # Time: O(logN)
        # Space: O(1)
        res = 0
        while n:
            res += n & 1
            n >>= 1
        return res

    def hammingWeight2(self, n: int) -> int:
        res = 0
        while n:
            res += 1
            n &= n - 1
        return res
```

#### [剑指 Offer 65]不用加减乘除做加法

[+1] = [00000001]原 = [00000001]反 = [00000001]补
[-1] = [10000001]原 = [11111110]反 = [11111111]补

正整数的补码与原码形式相同, n & 0xffffffff 得到一个数的补码
> 5: 0000 0101
> 6: 0000 0110

> 与运算：能找到两数的需要进位的位置, 异或运算：能找到非进位位置
> 5&6 = 0000 0100

Q: 写一个函数，求两个整数之和，要求在函数体内不得使用 “+”、“-”、“*”、“/” 四则运算符号。
> 输入: a = 1, b = 1  
> 输出: 2

```python
class Solution:
    def add(self, a, b):
        x = 0xffffffff  # 32位数掩码
        a, b = a & x, b & x  # 求补码

        while b != 0:
            tmp = (a & b) << 1 & x
            a ^= b
            b = tmp

        # 结果是负数(>0x7FFFFFFF)的话再转成正常的 python 负数表示方式(~(a ^ 0xFFFFFFFF), 
        # 即先对低 32 位的取反, 更高位不变, 然后整体再取反, 从而将大于等于 32 位的数字重新转成 1)
        return a if a < 0x7fffffff else ~(a ^ x)
```

#### [剑指 Offer 56 - I]数组中数字出现的次数

Q: 一个整型数组 nums 里除两个数字之外，其他数字都出现了两次。请写程序找出这两个只出现一次的数字。
> 输入：nums = [1,2,10,4,1,4,3,3]
> 输出：[2,10] 或 [10,2]

```python
class Solution:
    def singleNumbers(self, nums: List[int]) -> List[int]:
        ''' 异或,相同的两个数字,异或为0. 0跟任何数字异或,都是本身
            如果一个数组中只有一个出现一次的数字,剩下都是出现两次的,我们寻找这个数字很简单
            只需要将所有的数字进行异或 ,最后得到的结果就是那个数字 
            以此方法，分成两组, 如果数字在该位上为0是一组,否则为另一组
        '''
        # Time: O(N)
        # Space: O(1)
        n, m = 0, 1
        for num in nums:
            n = n ^ num  # 找两个不同的数间，位置对应不同的二进制数

        while n ^ m == 0:  # 逐位异或， 找到左起第一个为1的位置，用于后续分组
            m <<= 1

        x, y = 0, 0

        for num in nums:
            if num & m == 1:
                x ^= num
            else:
                y ^= num
        return x, y
```

#### [剑指 Offer 56 - II]数组中数字出现的次数 II

Q: 在一个数组 nums 中除一个数字只出现一次之外，其他数字都出现了三次。请找出那个只出现一次的数字。

> 输入：nums = [9,1,7,9,7,9,7]
> 输出：1


```python
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        ''' 统计32位中  每个位置上1 的个数
            依次对32位每个位置上取余， 余下来则是那个只出现一次的数字。
        '''
        counts = [0] * 32
        for num in nums:
            for j in range(32):
                counts[j] += num & 1
                num >>= 1

        res, m = 0, 3
        for i in range(32):
            res <<= 1
            res |= counts[31 - i] % m
        return res if counts[31] % m == 0 else ~(res ^ 0xffffffff)

class Solution2:
    def singleNumber(self, nums: List[int]) -> int:
        ''' 状态机
        由于二进制只能表示 0, 10,1 ，因此需要使用两个二进制位来表示 33 个状态。设此两位分别为 two, one，则状态转换变为：
            00 → 01 → 10 → 00 → ⋯
        '''
        ones = 0  # 每个数的状态的二进制的个位
        two = 0  # 每个数的状态的二进制的十位
        for num in nums:
            ones = ones ^ num & ~twos
            twos = twos ^ num & ~ones
        return ones
```