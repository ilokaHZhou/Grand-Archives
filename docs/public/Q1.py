def quickSort(nums, left, right):
    if nums and left < right:
        mid = partition(nums, left, right)
        quickSort(nums, left, mid - 1)
        quickSort(nums, mid + 1, right)

def partition(arr, left, right):
    pivot = arr[right]
    i = left - 1
    for j in range(left, right):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[right] = arr[right], arr[i + 1]
    return i + 1

def test(arr, start, end):
    print('original:')
    print(arr)
    quickSort(arr, start, end)
    print('sorted:')
    print(arr)
    print()


a = [4, 5, 6, 2, 8, 1, 35, 63, 23, 73, 19, 100] 
test(a, 0, len(a) - 1)

b = []
test(b, 0, len(b) - 1)

c = None
test(c, 0, 0)

d = [0, 0, 0, 0]
test(d, 0, len(d) - 1)

e = [-9, -200, -3, -20, 0, 1, 5, 38, 23, 50]
test(e, 0, len(e) - 1)


