n1 = int(input("Enter size: "))
arr1 = list(map(int, input("Enter elements: ").split()))

def move_zeroes(arr):
    pos = 0
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[pos], arr[i] = arr[i], arr[pos]
            pos += 1
    return arr

print(move_zeroes(arr1))
