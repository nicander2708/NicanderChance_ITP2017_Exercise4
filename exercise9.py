def program(n):
    i = n

    while i >= 0:
        yield i
        i -= 1

for x in program(10):
    print(x)
