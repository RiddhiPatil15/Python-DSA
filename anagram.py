def anagram(s, t):
    return True if sorted(s) == sorted(t) else False

s = input("First string: ")
t = input("Second string: ")

print(anagram(s, t))