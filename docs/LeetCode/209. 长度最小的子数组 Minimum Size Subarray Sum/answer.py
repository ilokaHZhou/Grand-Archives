class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        array_length = len(nums)
        left, right, min_len, accumulation = 0, 0, float('inf'), 0
        while right < array_length:
            accumulation += nums[right]
            while accumulation >= target:
                subseq_length = right - left + 1
                min_len = min(min_len, subseq_length)
                accumulation -= nums[left]
                left += 1
            right += 1
        return min_len if min_len != float('inf') else 0