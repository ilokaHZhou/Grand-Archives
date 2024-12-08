# 冒泡排序 Bubble Sort

冒泡排序是一种简单的排序算法。它反复遍历要排序的元素列表，依次比较相邻的两个元素，如果它们的顺序错误就交换它们。遍历列表的工作是重复进行的，直到没有需要交换的元素为止。

在每次遍历中，最大的元素会“冒泡”到列表的最后。

**时间复杂度**:

- 最佳：O(n) （已经有序不用排，只需要一次遍历）
- 平均：O(n^2)
- 最差：O(n^2) （当数组是逆序排列时，每次比较后都需要交换，整体需要执行𝑛∗(𝑛−1)/2次操作）

**空间复杂度**: O(1)
**稳定性**: 稳定

Java:

```java
public class BubbleSortExample {
    public static void main(String[] args) {
        int[] array = {64, 34, 25, 12, 22, 11, 90};
        bubbleSort(array);
        System.out.println("Sorted array: ");
        printArray(array);
    }

    // 冒泡排序算法
    public static void bubbleSort(int[] array) {
        int n = array.length;
        for (int i = 0; i < n - 1; i++) {
            for (int j = 0; j < n - i - 1; j++) {
                if (array[j] > array[j + 1]) {
                    // 交换array[j]和array[j + 1]
                    int temp = array[j];
                    array[j] = array[j + 1];
                    array[j + 1] = temp;
                }
            }
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


Python:

```python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-1-i): # 待排序的元素，每次外层循环会把最大的数沉底，所以每轮相互比较的次数会比前一轮少一次
            if arr[j] > arr[j+1]: # 逐一比较相邻元素
                arr[j], arr[j+1] = arr[j+1], arr[j] # 交换元素

# 测试数据
arr = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(arr)

print("排序后的数组:")
for i in range(len(arr)):
    print("%d" % arr[i], end=" ")


```




