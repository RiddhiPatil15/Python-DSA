# n is a list containing numbers
# m is a list containing another set of number
# we need to print the number of times each of the elements from m appear in n

n = [5, 3, 2, 2, 1, 5, 5, 7, 5, 10]
m = [10, 11, 1, 9, 5, 6, 7, 2]

# using list

hash_list = [0]*(len(n)+1)
for num in n:
    hash_list[num]+=1

for num in m:
    if num<1 or num>len(n):
        print(0, end=" ")
    else:
        print(hash_list[num], end=" ")
print("\n")
# using frequency dictionary

freq_dict = {}
for num in n:
    freq_dict[num] = freq_dict.get(num, 0)+1
for num in m:
    print(freq_dict.get(num, 0), end=" ")

