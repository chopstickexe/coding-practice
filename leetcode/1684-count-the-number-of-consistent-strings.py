# https://leetcode.com/problems/count-the-number-of-consistent-strings/


class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        def _isConsistent(w: str) -> bool:
            return all([x in allowed for x in set(w)])
        return sum([_isConsistent(w) for w in words])