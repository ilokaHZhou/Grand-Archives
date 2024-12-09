public class Sort {
    public static void quickSort(int[] arr, int left, int right) {
        if (left < right) {

        }
    }

    public static int[] bubbleSort(int[] array) {
        int len = array.length;
        for (int i = 0; i < len; i++) {
            for (int j = 0; j < len - i - 1; j++) {
                if (array[j] > array[j + 1]) {
                    int temp = array[j];
                    array[j] = array[j + 1];
                    array[j + 1] = temp;
                }
            }
        }
        return array;
    }

    public static void quickSort2(int[] arr, int left, int right) {
        if (left < right) {
            int pivot = partition(arr, left, right);
            quickSort2(arr, left, pivot - 1);
            quickSort2(arr, pivot + 1, right);
        }
    }

    public static int partition(int[] arr, int left, int right) {
        int pivot = arr[left];
        int mark = left;
        for (int i = left + 1; i <= right; i++) {
            if (arr[i] < pivot) {
                mark++;
                int temp = arr[mark];
                arr[mark] = arr[i];
                arr[i] = temp;
            }
        }
        arr[left] = arr[mark];
        arr[mark] = pivot;
        return mark;
    }


    public static void main(String[] args) {
        int[] array = {10, 7, 8, 9, 1, 5, 3, 2};
        System.out.println("Original Array:" );
        for (int num : array) {
            System.out.print(num + " ");
        }

        int[] result = bubbleSort(array);

        // quickSort(array, 0, array.length - 1);
        quickSort2(array, 0, array.length - 1);

        System.out.println("\nSorted Array:" );
        for (int num : result) {
            System.out.print(num + " ");
        }
    }
}