from typing import List


class Solution:
    def find(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            if nums[0] == target:
                return 0
            elif nums[0] < target:
                return 1
            else:
                return -1
        else:
            index = len(nums) // 2
            if target < nums[index]:
                return self.find(nums[0:index], target)
            else:
                return index + self.find(nums[index:], target)

    def searchInsert(self, nums: List[int], target: int) -> int:
        ret = self.find(nums, target)
        if ret < 0:
            ret = 0
        return ret
