n = int(input("Enter num: "))

check = 0
num = n
while num>0:
    last = num%10
    check+=last*last*last
    num=num//10

if check == n:
    print("Armstrong")
else:
    print("Not Armstrong")

