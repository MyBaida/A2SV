class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        l = 0
        r = len(skill)-1
        
        total_skill = 0
        team = skill[l] + skill[r]

        while l < r:
            if skill[l] + skill[r] != team:
                return -1

            total_skill += skill[l]*skill[r]
            l += 1
            r -= 1

        return total_skill 