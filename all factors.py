from math import sqrt

n = int(input("Enter a number: "))
ans = set()
for i in range(1, int(sqrt(n))+1):
    if n%i==0:
        ans.add(i)
        ans.add(n//i)

result = list(ans)
result.sort()
for i in range(len(result)):
    print(result[i], end=" ")