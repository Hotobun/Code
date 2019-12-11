# 给定一个包含 m x n 个元素的矩阵（m 行, n 列），请按照顺时针螺旋顺序，返回矩阵中的所有元素。
# 输入:
# [
#  [ 1, 2, 3 ],
#  [ 4, 5, 6 ],
#  [ 7, 8, 9 ]
# ]
# 输出: [1,2,3,6,9,8,7,4,5]

class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        # 大佬解法:
        # r, i, j, di, dj = [], 0, 0, 0, 1
        # if matrix != []:
        #     for _ in range(len(matrix) * len(matrix[0])):
        #         r.append(matrix[i][j])
        #         matrix[i][j] = 0
        #         if matrix[(i + di) % len(matrix)][(j + dj) % len(matrix[0])] == 0:
        #             di, dj = dj, -di
        #         i += di
        #         j += dj
        # return r

        # 取首行 逆时针反转列表 递归取首行 返回
        if len(matrix) == 0:
            return
        elif len(matrix) == 1:
            return matrix
        elif len(matrix[0]) == 1:
            return [x[0] for x in matrix]
        result = matrix[0]
        


if __name__ == "__main__":
    s = Solution()
    args = [
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
    result = s.spiralOrder(args)
    print("result :\n",result)