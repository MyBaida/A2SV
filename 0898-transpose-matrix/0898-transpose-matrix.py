class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        col = 0
        copy_matrix = []

        while col < len(matrix[0]):
            output = []

            for row in range(len(matrix)):
                output.append(matrix[row][col])

            col += 1
            copy_matrix.append(output)  

        return copy_matrix