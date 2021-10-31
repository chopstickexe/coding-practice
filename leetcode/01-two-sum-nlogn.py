# https://leetcode.com/problems/two-sum/
# coded on my own

from collections import defaultdict
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = defaultdict(list)  # key: value in nums, value: original indices in nums 
        for i, n in enumerate(nums):
            indices[n].append(i)
        
        nums.sort()  # O(NlogN)
        for n in nums:  # O(N)
            i = indices[n][0]
            x = target - n
            if x in indices and indices[x][-1] != i:  # Has x and not at the same index
                return sorted([i, indices[x][-1]])
