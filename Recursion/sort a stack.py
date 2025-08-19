def sort_array(arr, n):
    if n == 0:
        return 0
    if n == 1:
        return
    for i in range(n-1):
        if arr[i] > arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]
    sort_array(arr, n-1)

arr = [64, 34, 25, 12, 22, 11, 90]
sort_array(arr, len(arr))
print("Sorted array: ", arr)