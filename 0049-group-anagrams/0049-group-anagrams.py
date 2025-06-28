class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        out = {}

        for word in strs:
            sorted_string = "".join(sorted(word))

            if sorted_string not in out:
                out[sorted_string] = []

            out[sorted_string].append(word)

        return [values for values in out.values()]