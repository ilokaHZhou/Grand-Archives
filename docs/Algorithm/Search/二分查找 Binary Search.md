# 二分查找 Binary Search

二分查找（Binary Search） 是一种高效的查找算法，用于在一个有序数组中快速找到目标值的索引。它的基本思想是通过不断将查找范围折半，从而大幅减少查找时间。

二分查找的步骤:

1.	初始设置：确定查找范围，设定左边界 left 和右边界 right。
2.	计算中间值：计算中间位置 mid = (left + right) // 2。
3.	比较中间值：
    - 如果 arr[mid] == target，返回 mid。
    - 如果 arr[mid] > target，则目标值在左半部分，更新右边界：right = mid - 1。
    - 如果 arr[mid] < target，则目标值在右半部分，更新左边界：left = mid + 1。
4.	继续查找：重复上述步骤，直到找到目标值，或查找范围为空（即 left > right）。
5.	返回结果：如果找到目标值，返回其索引；否则返回表示未找到的值（如 -1）。

## Python实现（递归）

```python
def binarySearch(arr, target, left, right):
    if left > right: # 未找到目标值
        return -1
    mid = (left + right) // 2
    if arr[mid] == target: # 找到目标值
        return mid
    elif arr[mid] > target:
        return binarySearch(arr, target, left, mid - 1)
    else: 
        return binarySearch(arr, target, mid + 1, right)

```

## Python实现（只用循环）

```python
def binarySearch(self, nums: List[int], target: int) -> int:
    i, j = 0, len(nums) - 1
    while i <= j:
        m = (i + j) // 2
        if target > nums[m]: i = m + 1
        elif target < nums[m]: j = m - 1
        else: return m # 找到目标值
    return -1 # 未找到目标值

```

## Java实现（递归）

```java
class Solution {
    public int search(int[] nums, int target) {
        if (nums.length > 0)
            return binarySearch(nums, target, 0, nums.length - 1);
        return -1;
    }

    public static int binarySearch(int[] arr, int target, int left, int right) {
        if (left > right) // 未找到目标值
            return -1;
        int m = (left + right) / 2;
        int midValue = arr[m];
        if (target == midValue) // 找到目标值
            return m;
        else if (target < midValue)
            return binarySearch(arr, target, left, m - 1);
        else
            return binarySearch(arr, target, m + 1, right);
    }
}
```



## Java实现（只用循环）

```java
class Solution {
    public int search(int[] nums, int target) {
        int i = 0, j = nums.length - 1;
        while(i <= j) {
            int m = (i + j) / 2;
            int midValue = nums[m];
            if (target < midValue)
                j = m - 1;
            else if (target > midValue)
                i = m + 1;
            else
                return m; // 找到目标值
        }
        return -1; // 未找到目标值
        
    }
}

```