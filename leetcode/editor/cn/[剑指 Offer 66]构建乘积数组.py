# 给定一个数组 A[0,1,…,n-1]，请构建一个数组 B[0,1,…,n-1]，其中 B[i] 的值是数组 A 中除了下标 i 以外的元素的积, 即 B[
# i]=A[0]×A[1]×…×A[i-1]×A[i+1]×…×A[n-1]。不能使用除法。 
# 
#  
# 
#  示例: 
# 
#  
# 输入: [1,2,3,4,5]
# 输出: [120,60,40,30,24] 
# 
#  
# 
#  提示： 
# 
#  
#  所有元素乘积之和不会溢出 32 位整数 
#  a.length <= 100000 
#  
#  Related Topics 数组 前缀和 👍 251 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def constructArr(self, a: [int]) -> [int]:
        ''' 本质上： 是计算 除对角线外的所有数 的 乘积 = 下三角 * 上三角
            [1,2,3,4,5]
            [1,1,3,4,5]
            [1,2,1,4,5]
            [1,2,3,1,5]
            [1,2,3,4,1]
        '''
        n = len(a)
        b = [1] * n
        c = [1] * n
        for i in range(1, n):
            b[i] = b[i - 1] * a[i - 1]  # b此时为下三角

        for i in range(n - 2, -1, -1):
            c[i] = c[i+1] * a[i + 1]

        print(b, c)
        res = [c[i] * b[i] for i in range(n)]
        return res


# leetcode submit region end(Prohibit modification and deletion)

if __name__ == '__main__':
    S = Solution()
    print(S.constructArr([1, 2, 3, 4, 5]))
