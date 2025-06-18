class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_length = 0
        max_character = 0

        freq = Counter()
        l = 0

        for r in range(len(s)):
            
            freq[s[r]] += 1
            max_character = max(max_character, freq[s[r]])

            while (r-l+1) - max_character > k:
                freq[s[l]] -= 1
                l += 1
            
            max_length = max(r-l+1, max_length)

        return max_length