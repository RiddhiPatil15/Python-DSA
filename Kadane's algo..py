def kadanesAlgo(arr):
    maxsum = arr[0]
    curr = arr[0]
    for i in range(1, len(arr)):
        curr = max(curr, arr[i]+curr)
        maxsum = max(curr, maxsum)
    return maxsum

arr = list(map(int, input("Enter elements: ").split()))
res = kadanesAlgo(arr)
print(res)