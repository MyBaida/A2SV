class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        position = []

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    position.append([i,j])

        for r,c in position:
            matrix[r] = [0] * len(matrix[0])

            for i in range(len(matrix)):
                matrix[i][c] = 0