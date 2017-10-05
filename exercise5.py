import math
add,sub,mult,div = range(4)
def calculator (a,b,calc=add,outformat=float):
    if calc == add:
        result = a + b
        print(result)
    elif calc == sub:
        result = a - b
        print(result)
    elif calc == mult:
        result = a * b
        print(result)
    elif calc == div:
        result = a / b
        print(result)
    else:
        raise ValueError

    if outformat == int:
        result = round(result)
        print(result)
    elif outformat == float:
        result = float(result)
    else:
        raise ValueError

    return result

calculator(2,3.0)
calculator(2,3.0,add,int)
calculator(2,3.0,div)
calculator(2,3.0,div,int)
