class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        r = 0
        n = len(nums)
        sum_val = nums[0]
        res = n + 1
        while l < n and r < n:
            if sum_val < target:
                r += 1
                if r >= n:
                    break
                sum_val += nums[r]
            elif sum_val >= target:
                res = min(r - l + 1, res)
                sum_val -= nums[l]
                l += 1
        if res == n + 1:
            return 0
        return res
