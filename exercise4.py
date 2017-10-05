def recursive(x):
    try:
        if x == 1:
            return 1
        else:
            return x * recursive(x-1)
    except (RecursionError, TypeError):
        return None

num = recursive(5)
print(num)
