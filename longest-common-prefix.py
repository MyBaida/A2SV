class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]

        for word in strs:
            if len(word) < len(prefix):
                prefix = word

        for word in strs:
            for i in range(len(prefix)):
                if word[i] != prefix[i]:
                    prefix = prefix[:i]
                    break

        return prefix
