from math import sqrt as _sqrt
from math import sin as _sin
from math import cos as _cos
from math import tan as _tan
from math import factorial as _factorial
from math import radians as _toDegrees
from math import log10 as _log10
from SearchFuncs import searchChar, searchSplittingComma, searchSigma

def calc(expr: str):
    try:
        return float(expr)
    except ValueError:
        pass

    idxAdd = searchChar(expr, '+')
    idxSub = searchChar(expr, '-')
    idxMul = searchChar(expr, '*')
    idxDiv = searchChar(expr, '/')
    idxPow = searchChar(expr, '^')
    idxFac = searchChar(expr, "!")
    idxSqrt = searchChar(expr, '√')
    idxNthroot = searchChar(expr, 'R')
    idxSin = searchChar(expr, "s")
    idxCos = searchChar(expr, "c")
    idxTan = searchChar(expr, "t")
    idxLog = searchChar(expr, "l")
    idxSum = searchChar(expr, "S")
    idxDif = searchChar(expr, "D")
    idxInt = searchChar(expr, "I")

    if idxAdd != -1:
        left = expr[:idxAdd]
        if idxAdd == 0:
            left = "0"
        right = expr[idxAdd+1:]
        return calc(left) + calc(right)

    elif idxSub != -1:
        left = expr[:idxSub]
        if idxSub == 0:
            left = "0"
        right = expr[idxSub+1:]
        return calc(left) - calc(right)

    elif idxMul != -1:
        left = expr[:idxMul]
        right = expr[idxMul+1:]
        return calc(left) * calc(right)

    elif idxDiv != -1:
        left = expr[:idxDiv]
        right = expr[idxDiv+1:]
        return calc(left) / calc(right)

    elif idxPow != -1:
        left = expr[:idxPow]
        right = expr[idxPow+1:]
        return calc(left) ** calc(right)

    elif idxFac != -1:
        left = expr[:idxFac]
        return _factorial(calc(left))

    elif idxSqrt != -1:
        right = expr[idxSqrt+1:]
        return _sqrt(calc(right))

    elif idxNthroot != -1:
        p = searchSplittingComma(expr, idxNthroot)
        a, b = expr[2:p], expr[p+1:-1]
        return calc(b) ** (1/calc(a))

    elif idxSin != -1:
        right = expr[idxSin+1:]
        return _sin(_toDegrees(calc(right)))

    elif idxCos != -1:
        right = expr[idxCos+1:]
        return _cos(_toDegrees(calc(right)))

    elif idxTan != -1:
        right = expr[idxTan+1:]
        return _tan(_toDegrees(calc(right)))

    elif idxLog != -1:
        p = searchSplittingComma(expr, idxLog)
        a, b = expr[2:p], expr[p+1:-1]
        return _log10(calc(b)) / _log10(calc(a))

    elif idxSum != -1:
        var, start, end, func = searchSigma(expr)

        start = round(calc(start))
        end = round(calc(end))
        Sum = 0
        for val in range(start, end+1):
            Sum += calc(func.replace(var, str(val)))
        return Sum

    elif idxDif != -1:
        pows = countXpowers(expr[2:-1])
        c_0 = calc(expr[2:-1].replace('x', '0'))
        result = ''
        for p in range(len(pows)):
            if pows[p] == 0:
                continue

            coef = pows[p]*(p+1)

            if pows[p] > 0:
                result += "+"
            if coef != 1:
                result += f"{coef}*"
            result += "x"
            if p != 1:
                result += f"^{p}"
        return result
        #return f"{c_0if}+{'+'.join(f'{pows[i]}*x^{i+1}' for i in range(len(pows)) if pows[i] != 0)}"

    elif idxInt != -1:
        pows = countXpowers(expr[2:-1])
        c_0 = calc(expr[2:-1].replace('x', '0'))
        result = ''
        if c_0 != 0:
            result = f"{c_0}*x"
        for p in range(len(pows)):
            if pows[p] == 0:
                continue
            coef = pows[p]


            if coef != 1 and p != 1:
                return -1
        return result

    elif expr[0] == "|":
        return abs(calc(expr[1:-1]))

    elif expr[0] == "(":
        right = expr[1:-1]
        return calc(right)


#if __name__ == "__main__":
# "(2*-√(5^2))^(1+1)" #input("Expr: ")# "-5*(3+2)++--+-+3"  # "13*-+(33+-+-+-+1)^13+(+--213)-+5------5-5-1-2-31-23-------+++-+-+++-12-32-34-123-5*13^2+5-5-(-10/(((3*-3+1)))-5*-13+2/(5-2+3*-5/-6)-5/-12*-31/23/234/-51/-23/(123/-3-3934591^2*-12374))^2"
                     # taylor series for sin(x) as n --> ∞
expr = "R(2,R(2,9))"  # "-S(n=0,80,(((-1)^n)/((2*n)!))*30^(2*n))" #"S(a=l(2,8),l(2,16),a*2)"  # "√(S(a=1,25,1))"  # "S(a=l(2,8),3,S(b=l(2,2^2),2,a*b+2))"  # "sin(√l(l(l(4,16),8),3^9)*10)"  # "6!/(5!*6+1)"
print("\n\n")
try:
    tree = calc((expr).replace("sqrt", '√') \
        .replace("sin", "s") \
        .replace("cos", "c") \
        .replace("tan", "t") \
        .replace(" ", ''))
    print("\n")
    #print("My answer:  ", tree)
    #print("Real answer:", eval(expr.replace("^", '**')))
except BaseException as e:
    raise e
    # input("press any key to exit")
