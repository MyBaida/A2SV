class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        output = []
        
        up = True
        i = 0
        j = 0

        while len(output) < len(mat)*len(mat[0]):
            if up:
                while i >= 0 and j < len(mat[0]):
                    output.append(mat[i][j])
                    i -= 1
                    j += 1

                if j >= len(mat[0]):
                    j -= 1
                    i += 2
                
                if i < 0:
                    i = 0

                up = False

            else:
                while j >= 0 and i < len(mat):
                    output.append(mat[i][j])
                    i += 1
                    j -= 1

                if i >= len(mat):
                    i -= 1
                    j += 2
                
                if j < 0:
                    j = 0

                up = True

        return output