def binaryoperation(s: str) -> int:
    if not s:
        return -1
    result = int(s[0])
    i = 1
    while i < len(s)-1:
        op = s[i]
        num = int(s[i+1])
        if op == 'A':
             result = result & num
        elif op == 'B':
            result = result | num
        elif op == 'C':
            result = result ^ num
        else:
            return -1
        i+=2

    return result

s = input("Enter binary string with operations: ")
print(binaryoperation(s))