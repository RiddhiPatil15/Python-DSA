def BinaryToDec(num):
    if num==0:
        return 0
    ans = 0
    base = 1
    while num > 0:
        last = num%10
        ans += last*base
        base *= 2
        num //= 10
    return ans

num1 = int(input("Enter a number: "))
print(BinaryToDec(num1))