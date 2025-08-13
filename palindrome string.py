def two_pointer(data):
    data = data.lower().replce(" ", "")
    left, right = 0, len(data)-1
    palindrome = True

    while left < right:
        if data[left] != data[right]:
            palindrome = False
            break
        left+=1
        right-=1
    return palindrome

def is_palindrome(data):
    data = data.lower().replace(" ", "")
    if len(data) <= 1:
        return True

    if data[0] == data[-1]:
        return is_palindrome(data[1 : -1])
    else:
        return False

word = input("Enter the string: ")
if is_palindrome(word):
    print("Palindrome")
else:
    print("Not a palindrome")

# direct method
word = word.lower().replace(" ", "")
if word == word[::-1]:
    print(True)
else:
    print(False)