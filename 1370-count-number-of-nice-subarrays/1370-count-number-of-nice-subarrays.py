class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        nums = [nums[i] % 2 for i in range(len(nums))]

        freq = Counter()
        freq[0] = 1
        
        prefix = 0
        count = 0

        for num in nums:
            prefix += num

            if (prefix - k) in freq:
                count += freq[prefix - k]

            freq[prefix] += 1

        return count

