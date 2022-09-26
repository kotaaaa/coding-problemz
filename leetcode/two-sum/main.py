# https://www.google.com/url?q=https://leetcode.com/problems/two-sum/&sa=D&source=editors&ust=1664197671410681&usg=AOvVaw1TzHXvmlfsOXd4r0uH886A
from bisect import bisect_right
from copy import copy


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_orig = copy(nums)
        nums.sort()
        for i in range(len(nums)):
            idx = bisect_left(nums[i + 1 :], target - nums[i])
            if idx + i + 1 >= len(nums):
                continue
            if nums[idx + i + 1] == target - nums[i]:
                break
        if nums[i] == nums[idx + i + 1]:
            return [j for j, x in enumerate(nums_orig) if x == nums[i]]
        else:
            return [nums_orig.index(nums[i]), nums_orig.index(nums[idx + i + 1])]
