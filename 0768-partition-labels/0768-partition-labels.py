class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        output = []
        last_occurrence = {}

        for i, letter in enumerate(s):
            last_occurrence[letter] = i

        start = 0
        end = 0

        for i, letter in enumerate(s):
            end = max(end, last_occurrence[letter])
            
            if i == end:
                output.append(end - start + 1)
                start = i + 1

        return output