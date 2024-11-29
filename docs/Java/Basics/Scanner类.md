# Scanner类

## 从控制台输入

从控制台读取用户输入：

```java
import java.util.Scanner;

public class ScannerExample {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter your name: ");
        String name = scanner.nextLine();
        System.out.println("Hello, " + name + "!");
    }
}

```

## 从文件读取

从文件中读取数据：

```java
import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class ScannerFileExample {
    public static void main(String[] args) {
        try {
            Scanner scanner = new Scanner(new File("example.txt"));
            while (scanner.hasNextLine()) {
                String line = scanner.nextLine();
                System.out.println(line);
            }
            scanner.close();
        } catch (FileNotFoundException e) {
            e.printStackTrace();
        }
    }
}


```

## 从字符串读取

从字符串中读取数据：

```java
public class ScannerStringExample {
    public static void main(String[] args) {
        String input = "1, 2, 3, 4, 5";
        Scanner scanner = new Scanner(input);
        scanner.useDelimiter(", ");
        while (scanner.hasNextInt()) {
            int number = scanner.nextInt();
            System.out.println(number);
        }
        scanner.close();
    }
}

```

## 基本数据类型读取

```java
public class ScannerBasicTypesExample {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter an integer: ");
        int intValue = scanner.nextInt();
        System.out.println("You entered: " + intValue);

        System.out.print("Enter a float: ");
        float floatValue = scanner.nextFloat();
        System.out.println("You entered: " + floatValue);

        System.out.print("Enter a boolean: ");
        boolean boolValue = scanner.nextBoolean();
        System.out.println("You entered: " + boolValue);
    }
}
```
