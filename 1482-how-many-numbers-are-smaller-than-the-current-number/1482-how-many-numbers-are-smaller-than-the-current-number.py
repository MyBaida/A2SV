class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        
        sorted_ = sorted(nums)

        return [sorted_.index(num) for num in nums]