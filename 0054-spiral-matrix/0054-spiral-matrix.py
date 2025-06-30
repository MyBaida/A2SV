class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])
        output = []
        
        top = 0
        right = n
        bottom = m
        left = 0

        while top < bottom and left < right:
            # top traversal
            for i in range(left, right):
                output.append(matrix[top][i])

            top += 1

            # right traversal
            for i in range(top, bottom):
                output.append(matrix[i][right-1])
            
            right -= 1

            if not(left < right and top < bottom):
                break
                
            # bottom traversal
            for i in range(right-1, left-1, -1):
                output.append(matrix[bottom-1][i])
            
            bottom -= 1

            # left traversal
            for i in range(bottom-1, top-1, -1):
                output.append(matrix[i][left])
            
            left += 1

        return output