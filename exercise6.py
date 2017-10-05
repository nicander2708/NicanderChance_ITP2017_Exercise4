import math
add,sub,mult,div = range(4)
def calculator (calc=add,outformat=float,*args):
    if not args:
        raise ValueError('one number required')

    result = args[0]

    for a in args[1:]:
        if calc == add:
            result += a
            print(result)
        elif calc == sub:
            result -= a
            print(result)
        elif calc == mult:
            result *= a
            print(result)
        elif calc == div:
            result /= a
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

calculator(6,3.0,div)
