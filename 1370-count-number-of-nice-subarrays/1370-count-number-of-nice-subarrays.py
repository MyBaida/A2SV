class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        freq = Counter()
        freq[0] = 1

        for i in range(len(nums)):
            nums[i] %= 2

        curr = 0
        res = 0
        for num in nums:
            curr += num

            res += freq[curr-k] 

            freq[curr] += 1

        return res