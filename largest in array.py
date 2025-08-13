n = int(input("Enter size: "))
arr = list(map(int, input("Enter elements: ").split()))
# for _ in range(n):
#     num = int(input())
#     arr.append(num)

def largest(arr1, n1):
    large = arr1[0]
    for i in range(n1):
        if arr1[i] > large:
            large = arr1[i]
    return large

print("Largest element is: ",largest(arr, n))