class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        rot_idx = 0
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[0]:
                left = mid + 1
            elif nums[mid] == nums[0]:
                if nums[mid] > nums[mid + 1]:
                    left += 1
                break
            else:
                right = mid
        rot_idx = left
        if nums[0] < nums[len(nums) - 1]:
            arr = nums[:]
            rot_idx = 0
        else:
            arr = nums[rot_idx:] + nums[:rot_idx]
        left = 0
        right = len(arr) - 1
        tar_idx = len(arr)
        while left <= right:
            if left == right and arr[left] != target:
                break
            mid = (left + right) // 2
            if arr[mid] < target:
                left = mid + 1
            elif arr[mid] == target:
                tar_idx = mid
                break
            else:
                right = mid
        if tar_idx == len(arr):
            return -1
        if target >= nums[0]:
            return (mid + rot_idx) % len(nums)
        if mid + rot_idx >= len(nums):
            return -1
        return mid + rot_idx
