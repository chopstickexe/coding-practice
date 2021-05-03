# https://leetcode.com/problems/robot-bounded-in-circle/
# これは知らないと書けない


class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        instructions = list(instructions)
        current = 0  # north=0, east=1, south=2, west=3
        i = j = 0
        for d in instructions:
            if d == "R":
                current = (current + 1) % 4
            elif d == "L":
                current = (current + 3) % 4
            else:  # "G"
                if current == 0:
                    j += 1
                elif current == 1:
                    i += 1
                elif current == 2:
                    j -= 1
                elif current == 3:
                    i -= 1
        if (i == 0 and j == 0) or current is not 0:
            return True
        return False
