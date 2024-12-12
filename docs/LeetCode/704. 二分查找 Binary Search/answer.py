class Solution:
    @staticmethod
    def binarySearch(arr, target, left, right):
        if left > right:
            return -1
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            return Solution.binarySearch(arr, target, left, mid - 1)
        else: 
            return Solution.binarySearch(arr, target, mid + 1, right)

    def search(self, nums: List[int], target: int) -> int:
        if (nums):
            return Solution.binarySearch(nums, target, 0, len(nums) - 1)
        return -1