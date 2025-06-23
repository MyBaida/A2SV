class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        baskets = defaultdict(int)
        max_length = 0

        l = 0
        
        for r in range(len(fruits)):
            baskets[fruits[r]] += 1

            while len(baskets) > 2:
                baskets[fruits[l]] -= 1

                if baskets[fruits[l]] == 0:
                    del baskets[fruits[l]]
                
                l += 1

            max_length = max(max_length, r-l+1)

        return max_length