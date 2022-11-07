> n 皇后问题：在一个 n * n 的棋盘上放置 n 个皇后，要求不能有两个皇后位于同一行、同一列，或同一条 45 度斜线上。问共有多少种放法？
>
> 还有一种问题是输出每一种放法？（即输出一个放法矩阵）

解法一（简单粗暴法）：

思路很清楚，采用一个数组记录每一行皇后放的位置，例如pos[2] =5, 代表第 2 行的皇后放在第 5 列。在试探下一个位置的皇后时，需与上面已经放好的皇后检查是否冲突。例如试探位置为（row, col）, 而而第 i 行已经有一个皇后放置在 (i, pos[i]),则需要从这三个方面进行检查，查看是否冲突。

1. 是否位于同一列： col = pos[i]
2. 是否位于右上到左下的斜线上（称为撇斜线）： col - pos[i] == i - row
3. 是否位于右上到左下的斜线上（称为捺斜线）： col - pos[i] == row - i

```python
def n_queens_method1(n):			# n棋盘大小
    pos = [0] * n                   # 已放置的皇后的列号 
    count = 0                       # 解法总数

    def DFS(row):                   # 递归函数，试探第 row 行皇后的位置
        global count
        for col in range(n):        # 依次试探每一列， 每个位置
            # 检查冲突
            ok = True
            for i in range(row):    # 检查前面row行中的每一行是否有冲突
                if col == pos[i] or col - pos[i] == row - i or col - pos[i] == i - row:
                    ok = False
                    break
            if not ok:
                continue
            # 检查冲突结束
            if row == n - 1:        # 已放到最后一行
                count += 1          # 找到一组解
            else:
                pos[row] = col      # 记录当前行皇后的位置
                DFS(row + 1)
                # pos[row] = 0  # 因为sol[row]在下一次被写之前不会被读，不要还原
	DFS(0)
```

```python
class Solution2:
    def solveNQueens(self, n: int) -> [[str]]:
        def generateBoard():
            board = list()
            for i in range(n):
                row[queens[i]] = "Q"
                board.append("".join(row))
                row[queens[i]] = "."
            return board

        def backtrack(row: int):
            if row == n:
                board = generateBoard()
                solutions.append(board)
            else:
                for i in range(n):
                    if i in columns or row - i in diagonal1 or row + i in diagonal2:
                        continue
                    queens[row] = i
                    columns.add(i)
                    diagonal1.add(row - i)
                    diagonal2.add(row + i)
                    backtrack(row + 1)
                    columns.remove(i)
                    diagonal1.remove(row - i)
                    diagonal2.remove(row + i)
                    
        solutions = list()
        queens = [-1] * n
        columns = set()
        diagonal1 = set()
        diagonal2 = set()
        row = ["."] * n
        backtrack(0)
        return solutions
```

解法二（空间换时间）：

简单粗暴法中，对于每一个试探位置，都需要逐个搜寻每一行已放的皇后，比较三个冲突条件，因此很慢。若是由一个额外的标识位单独记录下，试探位置的「竖」、「撇」、「捺」是否占用，就可以在O(1)的时间内，知道这个位置能不能放了。

因此，在调用DFS(row+1)之前，将试探位置的「竖」、「撇」、「捺」都标记为占用，调用返回后进行清除。

为了明确地指代每一条竖、撇、捺，需要给它们编号。一种编号方式如下图所示。竖一共有 n 条，编号为 0 至 n-1，跟列号相同；撇、捺各有 2n-1 条，编号为 0 至 2n-2。由行列坐标 (row, col) 求撇、捺编号的公式为：

- - 撇编号：row + col
- - 捺编号：n - 1 - row + col

- 为什么是这样的编号？因为只有这样编号才能保证处于同一撇或同一捺位置上的点的值相等，代表这些格子处于同一撇或同一捺中，这是一个规律。

```python
n = 13
shu = [False] * n               # 每一竖是否被占用
pie = [False] * (2 * n - 1)     # 每一撇是否被占用
na = [False] * (2 * n - 1)      # 每一捺是否被占用
count = 0

def DFS(row):
    global count
    for col in range(n):
        j = row + col
        k = n - 1 - row + col    # 当前位置所在的撇、捺编号
        if shu[col] or pie[j] or na[k]:         # 检查冲突
            continue
        if row == n - 1:
            count += 1
        else:
            shu[col] = pie[j] = na[k] = True    # 标记当前竖、撇、捺已被占用
            DFS(row + 1)
            shu[col] = pie[j] = na[k] = False   # 清除标记

DFS(0)
```

解法三：

解法二中，额外定义三个检查冲突的标志位的数组空间，采用时间换空间。

每一个**布尔变量**只携带 1 比特的信息，但一般的编程语言中都会用至少 1 个字节来存储一个布尔变量，有的语言中甚至会使用 4 个字节。能不能真正让一个布尔变量只占用 1 个**二进制位**呢？这就要用到位运算了。

> 与 (and):                      5 & 6 = 4        (101 & 110 = 100) 
>
> 或 (or):                       5 | 6 = 7        (101 | 110 = 111)
>
>  异或 (xor):                    5 ^ 6 = 3        (101 ^ 110 = 011) 
>
> 取反 (not / complement):       ~5 = -6          (~00000101 = 11111010) 
>
> 左移 :             5 << 2 = 20      (101 << 2 = 10100) 
>
> 右移:            5 >> 2 = 1       (101 >> 2 = 1)

lowbit操作:

> ```text
>      a = 00110100
>     ~a = 11001011  # 把 a 取反
>     -a = 11001100  # 把 a 取反再加 1
> a & -a = 00000100  # 保留a 中最后一位1
> a & a-1 = 00110000  # a 中最后一位1置0
> ```

```python
n = 13
shu = pie = na = 0
count = 0

def DFS(row):
    global count, shu, pie, na
    for col in range(n):
        j = row + col; 
        k = n - 1 - row + col
        if ((shu >> col) | (pie >> j) | (na >> k)) & 1:         # 检查冲突
            continue
        if row == n - 1:
            count += 1
        else:
            shu ^= (1 << col); pie ^= (1 << j); na ^= (1 << k)  # 标记占用
            DFS(row + 1)
            shu ^= (1 << col); pie ^= (1 << j); na ^= (1 << k)  # 清除标记

DFS(0)

```

参考： [N皇后五解](https://www.zhihu.com/search?q=n皇后&utm_content=search_suggestion&type=content)