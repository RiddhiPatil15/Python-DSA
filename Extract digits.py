n = int(input("enter num: "))

num = n
count = 0
while num>0:
    last = num%10
    print(last, end =" ")
    count+=1
    num=num//10
print("\n")
print(count)