class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        m = len(matrix)
        n = len(matrix[0])

        prefix_matrix = [[0] * (n+1) for _ in range(m+1)]

        for i in range(1, m+1):
            for j in range(1, n+1):
                
                prefix_matrix[i][j] = matrix[i-1][j-1] + prefix_matrix[i-1][j] + prefix_matrix[i][j-1] - prefix_matrix[i-1][j-1]

        self.prefix_matrix = prefix_matrix
        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        prefix_matrix = self.prefix_matrix

        return prefix_matrix[row2+1][col2+1] - prefix_matrix[row2+1][col1] - prefix_matrix[row1][col2+1] + prefix_matrix[row1][col1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)