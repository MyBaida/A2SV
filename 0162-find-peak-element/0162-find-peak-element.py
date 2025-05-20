class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        low = 0
        high = len(nums)-1

        while low <= high:
            mid = (low + high) // 2

            if low == high:
                return mid

            elif nums[mid] < nums[mid + 1]:
                low = mid + 1

            else:
                high = mid