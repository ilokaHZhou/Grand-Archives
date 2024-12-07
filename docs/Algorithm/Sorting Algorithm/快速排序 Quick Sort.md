# 快速排序 Quick Sort

快速排序（Quick Sort）是一种高效的排序算法，采用分治法（Divide and Conquer）策略。

解决步骤：

1. 选择枢轴（Pivot）
在快速排序中，首先选择一个枢轴元素（pivot）。枢轴可以是数组中的任意元素，比如头尾元素，中间位置元素或者随机位置元素。

2. 分区（Partition）
将数组重新排列，使得枢轴左边的所有元素都小于或等于枢轴，右边的所有元素都大于或等于枢轴。这一步的目标是找到枢轴在排序后的正确位置，并将数组分成两个子数组。

3. 递归排序子数组（Recursively Sort Sub-arrays）
对枢轴两侧的子数组进行递归排序。递归终止条件是子数组的大小为0或1，此时数组已经有序。


伪代码：
```md
QuickSort(arr[], low, high)
   if low < high
      // pi 是分区索引，arr[pi] 已经排好序
      pi = Partition(arr, low, high)

      // 递归地对左右子数组进行快速排序
      QuickSort(arr, low, pi - 1)
      QuickSort(arr, pi + 1, high)

Partition(arr[], low, high)
   pivot = arr[high] // 选择最右边的元素为枢轴
   i = (low - 1) // 较小元素的索引

   for j = low to high - 1
      if arr[j] <= pivot
         i = i + 1
         Swap arr[i] with arr[j]

   Swap arr[i + 1] with arr[high]
   return (i + 1)
```

## 时间复杂度

最佳：O(n) （已经有序不用排，只需要一次遍历）
平均：O(n^2)
最差：O(n^2) （当数组是逆序排列时，每次比较后都需要交换，整体需要执行𝑛∗(𝑛−1)/2次操作）


## Java:

```java
public class QuickSortExample {
    public static void main(String[] args) {
        int[] array = {64, 34, 25, 12, 22, 11, 90};
        quickSort(array, 0, array.length - 1);
        System.out.println("Sorted array:");
        printArray(array);
    }

    // 快速排序算法
    public static void quickSort(int[] array, int low, int high) {
        if (low < high) {
            int pi = partition(array, low, high);
            quickSort(array, low, pi - 1); // 递归排序左子数组
            quickSort(array, pi + 1, high); // 递归排序右子数组
        }
    }

    // 分区方法
    public static int partition(int[] array, int low, int high) {
        int pivot = array[high];
        int i = (low - 1);
        for (int j = low; j < high; j++) {
            if (array[j] < pivot) {
                i++;
                // 交换 array[i] 和 array[j]
                int temp = array[i];
                array[i] = array[j];
                array[j] = temp;
            }
        }
        // 交换 array[i + 1] 和 array[high] (或 pivot)
        int temp = array[i + 1];
        array[i + 1] = array[high];
        array[high] = temp;
        return i + 1;
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


## Python

（会创建新数组）:

```python
def quickSort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2] # 选取基准值，也可以选取第一个或最后一个元素，这里选择最中间的值
        left = [x for x in arr if x < pivot]
        middle = [y for y in arr if y == pivot]
        right = [z for z in arr if z > pivot]
        return quickSort(left) + middle + quickSort(right)

# 测试数据
arr = [64, 34, 25, 12, 22, 11, 90]
sorted_arr = quick_sort(arr)

print("排序后的数组:")
print(sorted_arr)

```

（不创建新数组）：

```python
def quickSort(arr, low, high):
    if low < high:
        pivot = partition(arr, low, high)
        quickSort(arr, low, pivot - 1)
        quickSort(arr, pivot + 1, high)

def partition(arr, low, high):
    pivot = arr[high] # 选取最右侧元素为枢轴
    i = low
    for j in range(low, high):
        if arr[j] < pivot:
            arr[j], arr[i] = arr[i], arr[j] # 交换元素，把小于pivot的值换到最前面去
            i = i + 1

    arr[i], arr[high] = arr[high], arr[i] # 把pivot的值换到中间来，小于pivot值子序列之后
    return i


# 测试数据
arr = [64, 34, 25, 12, 22, 11, 90]
quickSort(arr, 0, len(arr) - 1)

print("排序后的数组:")
print(arr)


```





## C++

```C++
#include <iostream>

using namespace std;

void Qsort(int arr[], int low, int high){
    if (high <= low) return;
    int i = low;
    int j = high;
    int key = arr[low];
    while (true)
    {
        /*从左向右找比key大的值*/
        while (arr[i] <= key)
        {
        	i++;
            if (i == high){
                break;
            }
        }
        /*从右向左找比key小的值*/
        while (arr[j] >= key)
        {
        	j--;
            if (j == low){
                break;
            }
        }
        if (i >= j) break;
        /*交换i,j对应的值*/
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }
    /*中枢值与j对应值交换*/
    arr[low] = arr[j];
    arr[j] = key;
    Qsort(arr, low, j - 1);
    Qsort(arr, j + 1, high);
}

int main()
{
    int a[] = {57, 68, 59, 52, 72, 28, 96, 33, 24};

    Qsort(a, 0, sizeof(a) / sizeof(a[0]) - 1);/*这里原文第三个参数要减1否则内存越界*/

    for(int i = 0; i < sizeof(a) / sizeof(a[0]); i++)
    	{
        cout << a[i] << " ";
    }
    
    return 0;
}/*参考数据结构p274(清华大学出版社，严蔚敏)*/
```




