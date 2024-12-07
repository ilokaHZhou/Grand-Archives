## ArrayList

`ArrayList`类是一个可以动态修改的数组，与普通数组的区别就是它是没有固定大小的限制，我们可以添加或删除元素。

`ArrayList`继承了`AbstractList`，并实现了`List`接口。

![img](/arrayList.png)

::: tip
`ArrayList`里可以加入null值。

`ArrayList`是由数组来实现数据存储的（名为`elementData`的`Object[]`）。

创建`ArrayList`对象时，如果使用的是无参构造器，则初始分配空间为0，第一次添加元素时空间会扩充到10，如需再次扩容，扩容`elementData`为原本的`1.5`倍；如果使用有参数的构造器，则分配空间为指定大小，同样再次需要扩容时变为原本的1.5倍。

`ArrayList`基本等同于`Vector`，但`ArrayList`线程不安全（执行效率高，因为没有安全控制，看源码，add方法里前面没有synchronized修饰符）因此多线程不建议使用。
:::

**创建一个 `ArrayList` 实例**:

```java
import java.util.ArrayList; // 引入 ArrayList 类

ArrayList<E> objectName = new ArrayList<>();　 // 初始化

// 以下两种写法都行
ArrayList<String> list = new ArrayList<String>();
ArrayList<String> list = new ArrayList<>();
```

常用功能：

- 使用`add`添加元素
- 使用`get`访问元素
- 使用`set`修改元素
- 使用`remove`删除元素
- 使用`size`获取列表大小
- 使用`Collections.sort`方法排序
- 使用`contains`方法看元素是否在ArrayList中
- 使用`indexOf`和`lastIndexOf`获得元素在集合中出现/最后一次出现的位置
- 使用`addAll(int index, Collection c)`从index位置将`Collection c`里所有元素添加进来
- 使用`sublist(int from_index, int to_index)`返回从`from_index`到`to_index`的子集合，左包右不包

```java
public class ArrayListExample {
    public static void main(String[] args) {
        ArrayList<String> list = new ArrayList<>();
        list.add("Apple"); // 添加元素
        list.add("Banana");

        int size = list.size(); // 获取列表大小
        System.out.println(size); // 2

        String fruit = list.get(1); // 访问第二个元素
        System.out.println(fruit); // 输出: Banana

        list.set(1, "Blueberry"); // 修改第二个元素
        System.out.println(list); // 输出: [Apple, Blueberry]

        list.remove(1); // 删除第二个元素
        System.out.println(list); // 输出: [Apple]
    }
}

```

```java
import java.util.ArrayList;
import java.util.Collections;

public class ArrayListExample {
    public static void main(String[] args) {
        ArrayList<String> list = new ArrayList<>();
        list.add("Banana");
        list.add("Apple");
        list.add("Cherry");
        Collections.sort(list); // 排序
        System.out.println(list); // 输出: [Apple, Banana, Cherry]

        boolean found = list.contains("Banana"); // 搜索元素
        System.out.println(found);

        int index = list.indexOf("Banana"); // 获取"Banana"第一次出现的索引
        System.out.println(index); // 输出: 1
        int lastIndex = list.lastIndexOf("Banana"); // 获取"Banana"最后一次出现的索引
        System.out.println(lastIndex); // 输出: 1


        ArrayList<String> list1 = new ArrayList<>();
        list1.add("Apple");
        list1.add("Banana");

        ArrayList<String> list2 = new ArrayList<>();
        list2.add("Cherry");
        list2.add("Date");

        list1.addAll(list2); // 将list2的所有元素添加到list1中
        System.out.println(list1); // 输出: [Apple, Banana, Cherry, Date]


        ArrayList<String> list = new ArrayList<>();
        list.add("Apple");
        list.add("Banana");
        list.add("Cherry");
        list.add("Date");
        ArrayList<String> subList = new ArrayList<>(list.subList(1, 3)); // 获取索引1到3之间的子列表 index 1包含 3不包含
        System.out.println(subList); // 输出: [Banana, Cherry]
    }
}

```

## LinkedList

链表（Linked list）是一种常见的基础数据结构，是一种线性表，但是并不会按线性的顺序存储数据，而是在每一个节点里存到下一个节点的地址。

链表可分为单向链表和双向链表。Java里LinkedList是双向链表。

![img](/linkedList.png)

### Node类与双向链表

```java
public class Node {
    int data; // 存储节点的数据
    Node prev; // 指向前一个节点
    Node next; // 指向下一个节点

    // 构造方法
    public Node(int data) {
        this.data = data;
        this.prev = null;
        this.next = null;
    }
}

```

这个`Node`类包括：

- `data`字段，用于存储节点的数据。

- `prev`字段，用于指向前一个节点。

- `next`字段，用于指向下一个节点。

构造方法，用于初始化节点的数据，并将前一个和下一个节点的引用设置为null。

以下是如何使用Node类创建一个简单的双向链表的示例：

```java
public class DoublyLinkedList {
    Node head; // 链表的头节点

    // 在链表末尾添加一个节点
    public void append(int data) {
        Node newNode = new Node(data);
        if (head == null) {
            head = newNode;
        } else {
            Node current = head;
            while (current.next != null) {
                current = current.next;
            }
            current.next = newNode;
            newNode.prev = current;
        }
    }

    // 遍历并打印链表中的节点
    public void printList() {
        Node current = head;
        while (current != null) {
            System.out.print(current.data + " ");
            current = current.next;
        }
        System.out.println();
    }

    public static void main(String[] args) {
        DoublyLinkedList list = new DoublyLinkedList();
        list.append(1);
        list.append(2);
        list.append(3);
        list.printList(); // 输出: 1 2 3
    }
}

```


**创建一个 `LinkedList` 实例**:

```java
import java.util.LinkedList;

public class LinkedListExample {
    public static void main(String[] args) {
        LinkedList<String> list = new LinkedList<>();
    }
}

```

### 增删改查

```java
public class LinkedListExample {
    public static void main(String[] args) {
        LinkedList<String> list = new LinkedList<>();
        list.add("Apple");
        list.add("Banana");
        System.out.println(list); // 输出: [Apple, Banana]

        // 添加第一个和最后一个元素:
        LinkedList<String> list2 = new LinkedList<>();
        list2.addFirst("Apple");
        list2.addLast("Banana");
        System.out.println(list2); // 输出: [Apple, Banana]

        String fruit = list.get(1); // 访问第二个元素
        System.out.println(fruit); // 输出: Banana

        String first = list.getFirst(); // 访问第一个元素
        String last = list.getLast(); // 访问最后一个元素
        System.out.println(first); // 输出: Apple
        System.out.println(last); // 输出: Banana

        list.set(1, "Blueberry"); // 修改第二个元素
        System.out.println(list); // 输出: [Apple, Blueberry]

        list.remove(1); // 删除第二个元素
        System.out.println(list); // 输出: [Apple]

        int size = list.size(); // 获取列表大小
        System.out.println(size); // 输出: 1
    }
}

```

### 迭代

```java
public class LinkedListExample {
    public static void main(String[] args) {
        LinkedList<String> list = new LinkedList<>();
        list.add("Apple");
        list.add("Banana");
        
        // 使用 for 循环迭代
        for (int i = 0; i < list.size(); i++) {
            System.out.println(list.get(i));
        }
        
        // 使用 for-each 循环迭代
        for (String fruit : list) {
            System.out.println(fruit);
        }

        // 使用 LinkedList 的迭代器循环迭代
        Iterator<String> iterator = list.iterator(); // 使用迭代器迭代 LinkedList
        while (iterator.hasNext()) {
            String fruit = iterator.next();
            System.out.println(fruit);
        }
    }
}
```


## Vector

**创建 `Vector` 实例**
```java
import java.util.Vector;

public class VectorExample {
    public static void main(String[] args) {
        Vector<String> vector = new Vector<>();
    }
}
```

### 增删改

```java
public class VectorExample {
    public static void main(String[] args) {
        Vector<String> vector = new Vector<>();
        vector.add("Apple");
        vector.add("Banana");
        System.out.println(vector); // 输出: [Apple, Banana]

        int size = vector.size(); // 获取Vector大小
        System.out.println(size); // 输出: 2

        String fruit = vector.get(1); // 访问第二个元素
        System.out.println(fruit); // 输出: Banana

        vector.set(1, "Blueberry"); // 修改第二个元素
        System.out.println(vector); // 输出: [Apple, Blueberry]

        vector.remove(1); // 删除第二个元素
        System.out.println(vector); // 输出: [Apple]
    }
}

```

迭代：

```java
import java.util.Enumeration;

public class VectorExample {
    public static void main(String[] args) {
        Vector<String> vector = new Vector<>();
        vector.add("Apple");
        vector.add("Banana");

        Enumeration<String> enumeration = vector.elements();
        while (enumeration.hasMoreElements()) {
            String fruit = enumeration.nextElement();
            System.out.println(fruit);
        }
    }
}
```