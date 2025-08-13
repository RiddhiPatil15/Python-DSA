def simple_fibo(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a+b

def recur_fibo(n):
    if n<= 1:
        return n
    return recur_fibo(n-1) + recur_fibo(n-2)

n = int(input("Enter number: "))
simple_fibo(n)

print("\n")

for i in range(n):
    print(recur_fibo(i), end=" ")

# using dp memoization
memo = {}
def fibo_dp(n):
    if n in memo:
        return memo[n]
    if n <= 1:
        memo[n] = n
    else:
        memo[n] = fibo_dp(n-1) + fibo_dp(n-2)
    return memo[n]

for i in range(n):
    print(fibo_dp(i), end=" ")
