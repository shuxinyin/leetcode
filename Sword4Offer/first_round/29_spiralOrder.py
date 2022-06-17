class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return list()

        rows, columns = len(matrix), len(matrix[0])
        order = list()
        left, right, top, bottom = 0, columns - 1, 0, rows - 1
        while left <= right and top <= bottom:
            #  上： 从左至右
            for column in range(left, right + 1):
                order.append(matrix[top][column])
            # 右： 从上之下
            for row in range(top + 1, bottom + 1):
                order.append(matrix[row][right])
            if left < right and top < bottom:
                # 下： 从右至左
                for column in range(right - 1, left, -1):
                    order.append(matrix[bottom][column])
                # 左： 从下至上
                for row in range(bottom, top, -1):
                    order.append(matrix[row][left])
            # 下一层
            left, right, top, bottom = left + 1, right - 1, top + 1, bottom - 1
        return order

