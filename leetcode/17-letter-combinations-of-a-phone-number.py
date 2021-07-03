from itertools import permutations
from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        d2l = {
            2: "abc",
            3: "def",
            4: "ghi",
            5: "jkl",
            6: "mno",
            7: "pqrs",
            8: "tuv",
            9: "wxyz",
        }

        ans = []

        def dfs(cur: str, i: int):
            if i >= len(digits):
                if len(cur) > 0:
                    ans.append(cur)
                return
            for l in d2l[int(digits[i])]:
                dfs(cur + l, i + 1)

        dfs("", 0)
        return ans
