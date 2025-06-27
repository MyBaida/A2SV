class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0] * n for _ in range(n)]

        top = 0
        bottom = n
        left = 0
        right = n
        num = 1

        while left < right and top < bottom:
            # Top traversal
            for i in range(left, right):
                matrix[top][i] = num
                num += 1

            top += 1

            # right traversal
            for i in range(top, bottom):
                matrix[i][right-1] = num
                num += 1

            right -= 1

            # bottom traversal
            for i in range(right-1, left-1, -1):
                matrix[bottom-1][i] = num
                num += 1

            bottom -= 1

            # left traversal
            for i in range(bottom-1, top-1, -1):
                matrix[i][left] = num
                num += 1

            left += 1

        return matrix