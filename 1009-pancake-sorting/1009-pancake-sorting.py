class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        n = len(arr)
        output = []

        for i in range(n):
            max_num = max(arr[:n-i])
            max_index = arr.index(max_num) + 1
            
            arr[:max_index] = reversed(arr[:max_index])
            output.append(max_index)

            arr[:n-i] = reversed(arr[:n-i])
            output.append(n-i)

        return output