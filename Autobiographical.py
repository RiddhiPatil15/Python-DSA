def autobiographical(num: str) -> bool:
    n = len(num)
    count = [0]*n
    for ch in num:
        d = int(ch)
        if d>= n:
            return False
        count[d] += 1
    for i in range(n):
        if int(num[i]) != count[i]:
            return False
    return True

num1 = input("Enter a number: ")
if autobiographical(num1):
    print(f"{num1} is an autobiographical number.")
else:
    print(f"{num1} is not an autobiographical number.")