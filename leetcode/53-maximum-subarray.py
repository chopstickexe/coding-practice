from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        global_max = nums[0]
        prev_max = nums[0]
        for i in range(1, len(nums)):
            n = nums[i]
            prev_max = max(prev_max + n, n)
            if global_max < prev_max:
                global_max = prev_max
        return global_max
