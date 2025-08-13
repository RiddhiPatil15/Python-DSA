n = int(input("Enter num: "))

num = n
rev = 0
while num>0:
    last = num%10
    rev = rev*10 + last
    num=num//10

if n == rev:
    print("Palindrome")
else:
    print("Not a palindrome")