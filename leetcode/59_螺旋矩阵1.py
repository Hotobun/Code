# 给定一个正整数 n，生成一个包含 1 到 n2 所有元素，且元素按顺时针顺序螺旋排列的正方形矩阵。
# 输入: 3
# 输出:
# [
#  [ 1, 2, 3 ],
#  [ 8, 9, 4 ],
#  [ 7, 6, 5 ]
# ]

class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if n == 1:
            return [1]
        k = n-1
        result = list()
        result = [[0 for _ in range(n)] for _ in range(n)]
        count = 1
        x = 0
        y = 0
        while k > 0:
            for i in range(k):
                i
                result[y][x] = count
                count += 1
                x += 1
            for i in range(k):
                result[y][x] = count
                count += 1
                y += 1
                i
            for i in range(k):
                result[y][x] = count
                count += 1
                x -= 1
                i
            for i in range(k):
                result[y][x] = count
                count += 1
                y -= 1
                i
            k -= 2
            x += 1
            y += 1
            if n%2 != 0:
                if k <= 0:
                    result[x][y] = count
        print(result)


if __name__ == "__main__":
    args = int(input("please input n:"))
    s = Solution()
    s.generateMatrix(args)
    