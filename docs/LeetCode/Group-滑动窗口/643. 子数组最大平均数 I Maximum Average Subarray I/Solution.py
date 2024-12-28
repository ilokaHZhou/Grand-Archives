# 通关滑动取平均的长度为k的窗口找最大值
class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        maxTotal = sum(nums[:k])
        total = maxTotal
        n = len(nums)

        for i in range(k, n):
            total = total - nums[i - k] + nums[i]
            maxTotal = max(maxTotal, total)
        return maxTotal / k