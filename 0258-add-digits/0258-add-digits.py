class Solution:
    def addDigits(self, num: int) -> int:
        def addNum(n):
            return sum(int(num) for num in str(n))

        while len(str(num)) != 1:
            num = addNum(num)

        return num