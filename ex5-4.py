def multi(*b):
    a = 1
    for i in b:
        a *= i
    return a
print(multi(3,4,5))
