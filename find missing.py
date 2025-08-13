def find(arr):
    n = len(arr)+1
    xorAll = 0
    xorArr = 0

    for i in range(1, n+1):
        xorAll ^= i

    for num in arr:
        xorArr ^= num

    return xorAll^xorArr

arr = list(map(int, input("Enter elements: ").split()))

print("The missing number: ", find(arr))
