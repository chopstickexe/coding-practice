from collections import defaultdict
from typing import List


# Basic solution: O(n) space complexity
class Solution01:
    def singleNumber(self, nums: List[int]) -> int:
        count = defaultdict(int)
        for n in nums:
            count[n] += 1

        for n in count:
            if count[n] == 1:
                return n


# Bit manipulation: O(1) space complexity
class Solution02:
    def singleNumber(self, nums: List[int]) -> int:
        a = 0
        for i in nums:
            a ^= i
        return a
