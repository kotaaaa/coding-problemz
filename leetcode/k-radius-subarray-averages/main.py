class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        ans = [-1 for _ in range(n)]
        if k == 0:
            return nums
        if 2 * k >= n:
            return ans
        sum_val = 0
        for i in range(2 * k + 1):
            sum_val += nums[i]
        ans[k] = sum_val // (2 * k + 1)
        for i in range(k + 1, n - k):
            sum_val -= nums[i - k - 1]
            sum_val += nums[i + k]
            ans[i] = sum_val // (2 * k + 1)
        return ans
