def print_subarray(arr):
    n = len(arr)
    for i in range(n):
        for j in range(i, n):
            print(arr[i:j+1])

# sub array sum:
def sum_subarray(arr):
    n = len(arr)
    for i in range(n):
        total = 0
        for j in range(i, n):
            total += arr[j]
            print(f"Subarray: {arr[i:j+1]}, Sum: {total}")

def max_subarraySum(arr):
    max_sum = arr[0]
    current = arr[0]

    for num in arr[1:]:
        current = max(num, current+num)
        max_sum = max(max_sum, current)
    return max_sum

arr = [1, 2, 3]
print_subarray(arr)
sum_subarray(arr)
max_subarraySum(arr)