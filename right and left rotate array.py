def right(arr, k):
    k %= len(arr)
    return arr[-k:] + arr[:-k]

def left(arr, k):
    k %= len(arr)
    return arr[k:] + arr[:k]

arr1 = [1, 2, 3, 4, 5]
k1 = 2

print("Right rotated: ", right(arr1, k1))
print("Left rotated: ", left(arr1, k1))