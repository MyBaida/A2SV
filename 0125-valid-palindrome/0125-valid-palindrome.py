class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_ = [i.lower() for i in s if i.isalnum()]

        l, r = 0, len(s_)-1

        while l < r:
            if s_[l] != s_[r]:
                return False
            l += 1
            r -= 1

        return True