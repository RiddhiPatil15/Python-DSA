def findCount(arr, num, diff):
    count = 0
    result = []
    for i in range(len(arr)):
        if abs(num - arr[i]) <= diff:
            count += 1
            result.append(arr[i])
    return count if count > 0 else -1

arr1 = list(map(int, input("Enter elements: ").split()))
num1 = int(input("Enter a number: "))
diff1 = int(input("Enter a difference: "))
print(findCount(arr1, num1, diff1))