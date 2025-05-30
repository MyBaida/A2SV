class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        max_element = -1

        for i in range(len(arr)-1, -1, -1):
            temp = arr[i]
            arr[i] = max_element
            max_element = max(temp, max_element)

        return arr