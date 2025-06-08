class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse = True)
        mine = 0

        l = 0
        r = len(piles)-1

        while l < r:
            l += 1
            mine += piles[l]

            l += 1
            r -= 1

        return mine