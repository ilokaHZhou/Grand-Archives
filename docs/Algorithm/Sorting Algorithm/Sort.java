public class Sort {
    public static void quickSort(int[] arr, int left, int right) {
        if (left < right) {

        }
    }


    public static void main(String[] args) {
        int[] array = {10, 7, 8, 9, 1, 5};
        System.out.println("Original Array:" );
        for (int num : array) {
            System.out.print(num + " ");
        }

        quickSort(array, 0, array.length - 1);

        System.out.println("\nSorted Array:" );
        for (int num : array) {
            System.out.print(num + " ");
        }
    }
}