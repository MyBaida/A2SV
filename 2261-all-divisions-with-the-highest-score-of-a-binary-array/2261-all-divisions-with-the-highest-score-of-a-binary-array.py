class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        ones = nums.count(1)
        zeroes = 0
        max_score = ones
        
        score_index = defaultdict(int)
        score_index[0] = ones

        for i in range(len(nums)):
            if nums[i] == 0:
                zeroes += 1

            else:
                ones -= 1
                
            score = zeroes + ones
            score_index[i+1] = score
            max_score = max(score, max_score)

        return [num for num in score_index if score_index[num] == max_score]