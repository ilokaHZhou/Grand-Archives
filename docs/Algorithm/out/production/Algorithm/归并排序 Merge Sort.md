# 归并排序 Merge Sort

归并排序（Merge Sort）是一种高效的排序算法，采用分治法（Divide and Conquer）的思想。其主要思想是将数组分成较小的部分，分别排序后再合并，最终得到有序数组。以下是归并排序的步骤和原理：

解决步骤：

1. 递归分割：

- 如果数组的长度大于1，则将数组分成两部分：
  - 左半部分：从起始位置到中间位置。
  - 右半部分：从中间位置到末尾位置。
- 对左右两部分分别进行递归分割，直到每个子数组的长度为1。

2. 合并排序：

- 合并两个已排序的子数组成一个有序数组。
- 合并时，从两个子数组的起始位置开始比较，较小的元素放入结果数组，然后移动指针到下一位置继续比较，直到所有元素都合并完成。


**时间复杂度**:

- 最佳：
- 平均：
- 最差：

**空间复杂度**: 
**稳定性**: 


## Java实现

```java
public class MergeSortExample {
    public static void main(String[] args) {
        int[] array = {64, 34, 25, 12, 22, 11, 90};
        mergeSort(array, 0, array.length - 1);
        System.out.println("Sorted array:");
        printArray(array);
    }

    // 归并排序算法
    public static void mergeSort(int[] array, int left, int right) {
        if (left < right) {
            int middle = (left + right) / 2;

            // 递归排序左右子数组
            mergeSort(array, left, middle);
            mergeSort(array, middle + 1, right);

            // 合并排序后的子数组
            merge(array, left, middle, right);
        }
    }

    // 合并两个子数组的方法
    public static void merge(int[] array, int left, int middle, int right) {
        int n1 = middle - left + 1;
        int n2 = right - middle;

        // 创建临时数组
        int[] L = new int[n1];
        int[] R = new int[n2];

        // 拷贝数据到临时数组
        for (int i = 0; i < n1; ++i) {
            L[i] = array[left + i];
        }
        for (int j = 0; j < n2; ++j) {
            R[j] = array[middle + 1 + j];
        }

        // 归并临时数组
        int i = 0, j = 0;
        int k = left;
        while (i < n1 && j < n2) {
            if (L[i] <= R[j]) {
                array[k] = L[i];
                i++;
            } else {
                array[k] = R[j];
                j++;
            }
            k++;
        }

        // 拷贝剩余元素
        while (i < n1) {
            array[k] = L[i];
            i++;
            k++;
        }
        while (j < n2) {
            array[k] = R[j];
            j++;
            k++;
        }
    }

    // 打印数组
    public static void printArray(int[] array) {
        for (int i = 0; i < array.length; i++) {
            System.out.print(array[i] + " ");
        }
        System.out.println();
    }
}

```

## Python实现

```python
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2  # 中间点
        left_half = arr[:mid]  # 左半部分
        right_half = arr[mid:]  # 右半部分

        # 递归排序两部分
        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        # 归并两部分
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # 处理剩余元素
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

# 测试数据
arr = [64, 34, 25, 12, 22, 11, 90]
merge_sort(arr)

print("排序后的数组:")
print(arr)

```