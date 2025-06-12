class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        sum_ = sum(nums[:k])
        max_sum = sum_

        for i in range(len(nums)-k):
            sum_ += nums[i+k] - nums[i]

            max_sum = max(max_sum, sum_)

        return max_sum/k