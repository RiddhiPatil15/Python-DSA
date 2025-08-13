import sys

n = int(input("Enter size: "))
arr = list(map(int, input("Enter the elements: ").split()))

def sec_largest(arr1, n1):
    second = -sys.maxsize
    large = arr1[0]
    for i in range(1, n1):
        if arr[i] > large:
            second = large
            large = arr[i]
        if (arr[i] < large) and (arr[i] > second):
            second = arr[i]
    return second

print("The second largest number is: ", sec_largest(arr, n))