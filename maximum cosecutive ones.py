arr = list(map(int, input("Enter numbers: ").split()))

count = 0
max_count = 0
for num in arr:
    if num == 1:
        count += 1
        max_count = max(max_count, count)
    else:
        count = 0

print("Maximum consecutive ones: ", max_count)