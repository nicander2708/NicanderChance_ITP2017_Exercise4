from math import sqrt
def hypotenuse(a,b):
    try:
        return sqrt(a**2+b**2)
    except TypeError:
        return None

result = hypotenuse(2,5)
print(result)
result = hypotenuse('2','4')
print(result)
result = hypotenuse(2,'4')
print(result)
