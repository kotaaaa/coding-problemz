# https://leetcode.com/problems/sum-of-even-numbers-after-queries/
class Solution:
    def sumEvenAfterQueries(
        self, nums: List[int], queries: List[List[int]]
    ) -> List[int]:
        sum_val = 0
        for i in nums:
            if i % 2 == 0:
                sum_val += i
        ans = [0 for _ in range(len(nums))]

        for i, query in enumerate(queries):

            a, b = query
            if (nums[b] % 2 == 0) and a % 2 == 0:
                sum_val += a
            elif (nums[b] % 2 == 1) and a % 2 == 0:
                pass
            elif (nums[b] % 2 == 0) and a % 2 != 0:
                sum_val -= nums[b]
            else:
                sum_val += nums[b] + a
            nums[b] += a
            ans[i] = sum_val
        return ans
