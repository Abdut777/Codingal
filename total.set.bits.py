def totalsetbits (n):
    count = 0
    while (n):
        if(n & 1 ==1):
            count += 1
        n >>= 1

    return count

print(totalsetbits (9)) 