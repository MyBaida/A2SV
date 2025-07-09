class Solution:
    def reverseString(self, s: List[str]) -> None:
      
        first = 0
        last = -1
        middle = len(s)//2

        while first < len(s):
            if  first == middle:
                break

            else:
                s[first],s[last] = s[last],s[first]

            first += 1
            last -= 1
        