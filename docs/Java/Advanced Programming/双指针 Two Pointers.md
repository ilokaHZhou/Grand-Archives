# 双指针

双指针（Two Pointers）是一种常用的编程技巧，常用于解决涉及数组或链表的问题。其基本思想是使用两个指针同时遍历数据结构，从而在一次遍历中解决问题。这种方法通常用于：

- 寻找数组中满足特定条件的两个元素
- 处理有序数组
- 反转链表
- 查找子数组或子序列

双指针的常见用法

- 左右指针：用于从数组两端向中间遍历。
- 快慢指针：用于在链表中寻找中间节点或检测环。

## 示例1：寻找数组中两个数之和为目标值

```java
import java.util.Arrays;

public class TwoSum {
    public static void main(String[] args) {
        int[] nums = {2, 7, 11, 15};
        int target = 9;
        int[] result = twoSum(nums, target);
        System.out.println(Arrays.toString(result)); // 输出: [0, 1]
    }

    public static int[] twoSum(int[] nums, int target) {
        int left = 0;
        int right = nums.length - 1;
        while (left < right) {
            int sum = nums[left] + nums[right];
            if (sum == target) {
                return new int[]{left, right};
            } else if (sum < target) {
                left++;
            } else {
                right--;
            }
        }
        return new int[]{-1, -1}; // 未找到
    }
}

```

## 示例2：反转链表

```java
public class ListNode {
    int val;
    ListNode next;
    ListNode(int val) { this.val = val; }

    public static ListNode reverseList(ListNode head) {
        ListNode prev = null;
        ListNode current = head;
        while (current != null) {
            ListNode nextTemp = current.next;
            current.next = prev;
            prev = current;
            current = nextTemp;
        }
        return prev;
    }

    public static void printList(ListNode head) {
        ListNode current = head;
        while (current != null) {
            System.out.print(current.val + " ");
            current = current.next;
        }
        System.out.println();
    }

    public static void main(String[] args) {
        ListNode head = new ListNode(1);
        head.next = new ListNode(2);
        head.next.next = new ListNode(3);
        head.next.next.next = new ListNode(4);
        head.next.next.next.next = new ListNode(5);

        printList(head); // 输出: 1 2 3 4 5
        ListNode reversedHead = reverseList(head);
        printList(reversedHead); // 输出: 5 4 3 2 1
    }
}

```


## 示例3：寻找链表的中间节点

```java
public class MiddleOfLinkedList {
    public static void main(String[] args) {
        ListNode head = new ListNode(1);
        head.next = new ListNode(2);
        head.next.next = new ListNode(3);
        head.next.next.next = new ListNode(4);
        head.next.next.next.next = new ListNode(5);

        ListNode middle = findMiddle(head);
        System.out.println(middle.val); // 输出: 3
    }

    public static ListNode findMiddle(ListNode head) {
        ListNode slow = head;
        ListNode fast = head;
        while (fast != null && fast.next != null) {
            slow = slow.next;
            fast = fast.next.next;
        }
        return slow;
    }
}

```