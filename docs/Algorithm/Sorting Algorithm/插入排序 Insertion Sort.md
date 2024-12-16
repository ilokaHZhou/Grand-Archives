# 插入排序

插入排序（Insertion Sort）是一种简单直观的排序算法，其核心思想是将数组分为已排序部分和未排序部分，每次从未排序部分取出一个元素，将其插入到已排序部分的正确位置，直到整个数组有序。

**步骤**:
1. 从第二个元素开始（假设第一个元素是已排序的）将当前元素与已排序部分的元素进行比较，从后向前找到合适的位置。
2. 将当前元素插入到该位置。并将其余待排序元素向后移动。
3. 重复上述步骤，直到遍历所有元素。

**时间复杂度**

最佳情况：当数组已接近排序，仅需 O(n) 次比较。
最差情况：当数组完全逆序，需要 O(n²) 次比较和交换。
平均情况：时间复杂度为 O(n²)。

**算法特点**

稳定性：插入排序是稳定的算法，因为不会改变相同元素的相对位置。
适用场景：适合小规模数据集或接近排序的数据。
劣势：对于大规模数据集，效率较低。


## Python实现

```python
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]  # 当前待插入的元素
        j = i - 1
        # 将大于 key 的元素向后移动
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key  # 插入元素到正确位置
    return arr

# 测试
arr = [12, 11, 13, 5, 6]
sorted_arr = insertion_sort(arr)
print("排序后:", sorted_arr)
```


## Java实现

```java
public class InsertionSort {
    public static void insertionSort(int[] arr) {
        for (int i = 1; i < arr.length; i++) {
            int key = arr[i];  // 当前待插入的元素
            int j = i - 1;

            // 将大于 key 的元素向后移动
            while (j >= 0 && arr[j] > key) {
                arr[j + 1] = arr[j];
                j--;
            }

            // 插入元素到正确位置
            arr[j + 1] = key;
        }
    }

    public static void main(String[] args) {
        int[] arr = {12, 11, 13, 5, 6};
        insertionSort(arr);

        // 输出结果
        System.out.print("排序后: ");
        for (int num : arr) {
            System.out.print(num + " ");
        }
    }
}

```

