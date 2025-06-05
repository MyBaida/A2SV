class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        while k:
            ans = nums.pop()
            nums.insert(0, ans)
            k -= 1