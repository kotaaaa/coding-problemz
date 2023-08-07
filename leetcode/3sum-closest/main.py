class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        n = len(nums)
        val = 0
        ans = 10**9
        for i in range(n - 2):
            val += nums[i]
            for j in range(i + 1, n - 1):
                val += nums[j]
                left = j + 1
                right = n - 1
                while left <= right:
                    mid = (left + right) // 2
                    if val + nums[mid] == target:
                        ans = val + nums[mid]
                        break
                    elif val + nums[mid] > target:
                        right = mid - 1
                    else:
                        left = mid + 1
                    if abs(ans - target) > abs(val + nums[mid] - target):
                        ans = val + nums[mid]
                val -= nums[j]
            val -= nums[i]
        return ans
