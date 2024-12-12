from typing import List


class Solution:
    def binarySearch(arr, target, left, right):
        if left > right:
            return -1
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            return binarySearch(arr, target, left, mid - 1)
        else: 
            return binarySearch(arr, target, mid + 1, right)

    def search(self, nums: List[int], target: int) -> int:
        if (nums):
            return self.binarySearch(nums, target, 0, len(nums))
        return -1