# https://leetcode.com/problems/valid-parentheses/


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        ps = {"(": ")", "{": "}", "[": "]"}
        for c in list(s):
            if c in set(ps.keys()):
                stack.append(c)
            elif c in set(ps.values()):
                if len(stack) == 0:
                    return False
                s = stack.pop()
                if c != ps.get(s):
                    return False
        if len(stack) != 0:
            return False
        return True