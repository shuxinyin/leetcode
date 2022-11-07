## 字符串

[剑指 Offer 05]替换空格

[剑指 Offer 19]正则表达式匹配
[剑指 Offer 20]表示数值的字符串
[剑指 Offer 67]把字符串转换成整数

[剑指 Offer 43]1～n 整数中 1 出现的次数
[剑指 Offer 44]数字序列中某一位的数字

[剑指 Offer 58 - I]翻转单词顺序
[剑指 Offer 58 - II]左旋转字符串

[剑指 Offer 67]把字符串转换成整数



#### [剑指 Offer 05]替换空格

> 请实现一个函数，把字符串 s 中的每个空格替换成"%20"。 
>  示例 1： 
>  输入：s = "We are happy."
>  输出："We%20are%20happy." 


```python
class Solution:
    def replaceSpace(self, s: str) -> str:
        res = []

        for c in s:
            if c == " ":
                res.append("%20")
            else:
                res.append(c)
        return ''.join(res)
```


#### [剑指 Offer 19]正则表达式匹配

Q: 请实现一个函数用来匹配包含'. '和'*'的正则表达式。模式中的字符'.'表示任意一个字符，而'*'表示它前面的字符可以出现任意次（含0次）。
在本题中，匹配是指字符串的所有字符匹配整个模式。例如，字符串"aaa"与模式"a.a"和"ab*ac*a"匹配，但与"aa.a"和"ab*a"均不匹配。 

> s = "aa"
> p = "a"
> 输出: false
> 解释: "a" 无法匹配 "aa" 整个字符串。

> s = "aab"  
> p = "c*a*b"  
> 输出: true  
> 解释: 因为 '*' 表示零个或多个，这里 'c' 为 0 个, 'a' 被重复一次。因此可以匹配字符串 "aab"。  

```python
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        ''' 采用递归的方法来实现。
            递归结束的条件是：当p结束的时候s也结束，则返回true；p结束的时候s没结束，返回False。
            在判断的过程中有两种情况，
            如：s=aaa,p=a*aaa
            一种是p[1]为"*"，此时有两种可能:
                1. 忽略a*这两个字符, 因为可以出现0次, 匹配零个p[0](下一步为match[s,p[2:]])
                2. 是匹配上这个字符, 用递归的方式匹配下一个, 匹配多个p[0](这一步需要判断s[0]和p[0]是否匹配下一步为match(s[1:],p)，
            第二种p[1]不为"*"：
                只需要判断s[0]和p[0]是否匹配并且下一步为match(s[1:],p[1:])即可，s[0]和p[0]匹配的情况是s[0]==p[0]或者p[0]为“.”
        '''
        if not p:   
            return not s

        # p 与 s 头个字符能否匹配上
        first_match = (len(s)>0 and (s[0]==p[0] or p[0]=='.'))

        if len(p)>=2 and p[1]=='*':
            return self.isMatch(s,p[2:]) or (first_match and self.isMatch(s[1:],p))
        else:
            return first_match and self.isMatch(s[1:], p[1:])

```

#### [剑指 Offer 20]表示数值的字符串
Q: 请实现一个函数用来判断字符串是否表示数值（包括整数和小数）。 


> 输入：s = "    .1  "
> 输出：true

```python
class Solution:
    def isNumber(self, s: str) -> bool:
        ''' 有限状态机
        '''
        pass

```

#### [剑指 Offer 67]把字符串转换成整数

Q: 写一个函数 StrToInt，实现把字符串转换成整数这个功能。不能使用 atoi 或者其他类似的库函数。 
    注意：假如该字符串中的第一个非空格字符不是一个有效整数字符、字符串为空或字符串仅包含空白字符时，则你的函数不需要进行转换。 

> 输入: "   -42"
> 输出: -42
> 解释: 第一个非空白字符为 '-', 它是一个负号。我们尽可能将负号与后面所有连续出现的数字组合起来，最后得到 -42 。

> 输入: "4193 with words"
> 输出: 4193
> 解释: 转换截止于数字 '3' ，因为它的下一个字符不为数字。
```python
class Solution:
    def StrToInt(self, s):
        ''' 1. 首先找符号位，必定首位
            2. 接着找后面的数字位置
            3. 遍历直到非数字位停止。
        '''
            Sum = 0
            Sign = 1
            s = s.strip()
            for i,num in enumerate(s):
                if i == 0:
                    if s[i] == '+':
                        continue
                    elif s[i] == '-':
                        Sign = -1
                        continue
                if num >= '0' and num <= '9':
                    Sum = Sum * 10 + int(s[i])
                else:
                    return 0
            
            return Sign * Sum
```


#### [剑指 Offer 58 - I]翻转单词顺序
> 输入一个英文句子，翻转句子中单词的顺序，但单词内字符的顺序不变。为简单起见，标点符号和普通字母一样处理。例如输入字符串"I am a student. "，
> 则输出"student. a am I"。 
 
>  示例 1：  
>  输入: "the sky is blue"
> 输出: "blue is sky the"

>  示例 2： 
>  输入: "  hello world!  "
> 输出: "world! hello"
> 解释: 输入字符串可以在前面或者后面包含多余的空格，但是反转后的字符不能包括。

```python
class Solution:
    def reverseWords(self, s: str) -> str:
        '''DoublePointer
        # 因为需要翻过来，所以倒序
         例子： "a good   [p1]example[p2]"

        '''
        s = s.strip()
        res = []
        p1 = p2 = len(s) - 1
        while p1 >= 0:
            while p1 >= 0 and s[p1] != ' ':
                p1 -= 1
            res.append(s[p1 + 1:p2 + 1])
            # 跳跃连续空格
            while s[p1] == ' ':  
                p1 -= 1
            p2 = p1
        return ' '.join(res)
```

#### [剑指 Offer 58 - II]左旋转字符串

字符串的左旋转操作是把字符串前面的若干个字符转移到字符串的尾部。请定义一个函数实现字符串左旋转操作的功能。
比如，输入字符串"abcdefg"和数字2，该函数将返回左旋转两位得到的结果"cdefgab"。

>  示例 1： 
>  输入: s = "abcdefg", k = 2
> 输出: "cdefgab"
>  示例 2： 
>  输入: s = "lrloseumgh", k = 6
>  输出: "umghlrlose"

```python
class Solution:
    def reverseLeftWords(self, s: str, n: int) -> str:
        return s[n:] + s[:n]
```






#### [剑指 Offer 43] 1～n 整数中 1 出现的次数
Q:  输入一个整数 n ，求1～n这n个整数的十进制表示中1出现的次数。 
    例如，输入12，1～12这些整数中包含1 的数字有1、10、11和12，1一共出现了5次。 

>  输入：n = 12
>  输出：5

```python
class Solution:
    def countDigitOne(self, n: int) -> int:
        '''
            一个数字可以看做是 高位+当前位+低位
        '''
        pass
```


#### [剑指 Offer 44]数字序列中某一位的数字

Q: 数字以0123456789101112131415…的格式序列化到一个字符序列中。在这个序列中，第5位（从下标0开始计数）是5，第13位是1，第19位是4等等。

> 输入：n = 3
> 输出：3

```python
class Solution:
    def findNthDigit(self, n: int) -> int:
        ''' 找规律
        1.确定这个n位在几位数字中.
        2.确定这个n位在几位数字中的那一个数字中.
        3.确定这个n位在几位数字中的那一个数字中的那一位.
        '''
        # 位数， 起始数字， 数位
        digit, start, count = 1, 1, 9
        
        # 1. 确定n位在 几位数中
        while n>count:
            n -= count
            start *= 10
            digit += 1
            count = 9 * start * digit
        # 2. 确定n位在几位数字中的哪一个数字中
        num = start + (n-1)//digit
        return int(str(num)[(n-1) % digit])
```