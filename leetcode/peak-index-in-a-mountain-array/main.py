class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left = 1
        right = len(arr) - 2
        ans = 0
        while left <= right:
            mid = (right + left) // 2
            if arr[mid - 1] < arr[mid] and arr[mid] > arr[mid + 1]:
                ans = mid
                break
            elif arr[mid - 1] > arr[mid]:
                right = mid
            else:
                left = mid + 1
        return ans
