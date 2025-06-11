class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        arr = [num for num in range( int(math.sqrt(c))+1)]
        
        l = 0
        r = len(arr)-1

        while l <= r:
            if (arr[l]**2) + (arr[r]**2) == c:
                return True

            if (arr[l]**2) + (arr[r]**2) > c:
                r -= 1

            else:
                l += 1

        return False