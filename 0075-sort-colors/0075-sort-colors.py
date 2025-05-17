class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = [0] * (max(nums)+1)

        for num in nums:
            count[num] += 1

        j = 0
        for i, c in enumerate(count):
            while c > 0:
                nums[j] = i
                j+=1
                c-=1 