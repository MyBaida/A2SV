class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_ = [i.lower() for i in s if i.isalnum()]

        return s_ == s_[::-1]