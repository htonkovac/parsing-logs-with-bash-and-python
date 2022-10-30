def is_odd(n):
    while n != 0:
        if n%10 not in [1,3,5,7,9]:
            return False
        n = n//10
    return True
for i in range(1000,3001):
    if is_odd(i):
        print(i)


# [1,3,5,7,9]