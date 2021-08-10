from SearchFuncs import searchChar
from math import sqrt as _sqrt

def calc(expr: str):
    try:
        return int(expr)
    except ValueError:
        pass
    if expr == 'i':
        return expr

    idxAdd = searchChar(expr, '+')
    idxSub = searchChar(expr, '-')
    idxMul = searchChar(expr, '*')
    idxPow = searchChar(expr, '^')
    idxSqrt = searchChar(expr, '√')

    if idxAdd != -1:
        left = calc(expr[:idxAdd])
        right = calc(expr[idxAdd+1:])

        calcLeft = calc(left)
        
        if type(calcLeft) is str and '+' in calcLeft:

            l, r = calcLeft.split('+')
            if 'i' in l and 'i' not in r:

                return f"i+{calc(r)+calc(right)}"
        return calcLeft

    elif idxSub != -1:
        left = calc(expr[:idxSub])
        right = calc(expr[idxSub+1:])

        if type(left) is str and type(right) is not str:
            return f"{right}-{left}"
        elif type(left) is not str and type(right) is str:
            return f"{left}-{right}"
        elif str not in (type(right), type(left)):
            return right-left
        else:
            # both contain i
            return NotImplemented

    elif idxMul != -1:
        left = calc(expr[:idxMul])
        right = calc(expr[idxMul+1:])
        if type(left) is not str and type(right) is str:
            return f"{left}*i"
        elif type(right) is not str and type(left) is str:
            return f"{right}*i"
        elif str not in (type(right), type(left)):
            return right*left
        else:
            # both contain i
            return NotImplemented

    elif idxPow != -1:
        left = calc(expr[:idxPow])
        right = calc(expr[idxPow+1:])
        if type(right) is str and 'i' in right:
            raise ValueError("fuck you man.\nWhy you raising to the power of i?\nYou some kind of anarchist?")
        # assume for a sec rightVal is 2...
        if type(left) is str:
            real = calc(left[:left.index('i')-1])
            if right == 0:
                return 1
            elif right == 1:
                return left
            elif right == 2:
                return pow(real, 2) * -1
            elif right == 3:
                return f"{pow(real, 3) * -1}*i"
            else:
                raise ValueError("Cannot raise i to more than 3.")
        else:
            return pow(left, right)

    elif idxSqrt != -1:
        content = expr[idxSqrt+1:]
        val = calc(content)
        if val < 0:
            return f"{_sqrt(abs(val))}*i"
        else:
            return _sqrt(val)

    elif expr[0] == "(":
        right = expr[1:-1]
        return calc(right)


if __name__ == '__main__':
    expr = "i+2+3"

    print(calc(expr))
