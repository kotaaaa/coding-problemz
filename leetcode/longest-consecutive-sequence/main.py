class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest_streak = 0
        ans = 0
        for num in num_set:
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1

                while True:
                    current_num += 1
                    if current_num in num_set:
                        current_streak += 1
                    else:
                        break
                ans = max(ans, current_streak)
        return ans
