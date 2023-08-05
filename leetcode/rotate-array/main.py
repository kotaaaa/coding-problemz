class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        if k > len(nums):
            k = k % len(nums)
        if k == 0:
            return
        a = nums[-k:] + nums[: len(nums) - k]
        for i in range(len(a)):
            nums[i] = a[i]
