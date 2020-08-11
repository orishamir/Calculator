from cmath import sqrt as _sqrt
from math import sin as _sin
from math import cos as _cos
from math import radians as _toDegrees


def parseToTree(expr: str, debug):
    if debug:
        print(expr)
    try:
        return float(expr)
    except ValueError:
        pass

    idxAdd = searchPlus(expr)
    idxSub = searchMinus(expr)
    idxMul = searchDivMul(expr, '*')
    idxDiv = searchDivMul(expr, '/')
    idxPow = searchPow(expr)
    idxSqrt = searchSqrt(expr)
    idxSin = searchSinCos(expr, "S")
    idxCos = searchSinCos(expr, "C")

    if idxAdd != -1:
        left = expr[:idxAdd]
        if idxAdd == 0:
            left = "0"
        right = expr[idxAdd + 1:]
        return parseToTree(left, debug) + parseToTree(right, debug)

    elif idxSub != -1:
        left = expr[:idxSub]
        if idxSub == 0:
            left = "0"
        right = expr[idxSub + 1:]
        return parseToTree(left, debug) - parseToTree(right, debug)

    elif idxMul != -1:
        left = expr[:idxMul]
        right = expr[idxMul + 1:]
        return parseToTree(left, debug) * parseToTree(right, debug)

    elif idxDiv != -1:
        left = expr[:idxDiv]
        right = expr[idxDiv + 1:]
        return parseToTree(left, debug) / parseToTree(right, debug)

    elif idxPow != -1:
        left = expr[:idxPow]
        right = expr[idxPow + 1:]
        return parseToTree(left, debug) ** parseToTree(right, debug)

    elif idxSqrt != -1:
        right = expr[idxSqrt + 1:]
        print(right)
        return _sqrt(parseToTree(right, debug))
    elif idxSin != -1:
        right = expr[idxSin + 1:]
        print(right)
        return _sin(_toDegrees(parseToTree(right, debug)))

    elif idxCos != -1:
        right = expr[idxCos + 1:]
        print(right)
        return _cos(_toDegrees(parseToTree(right, debug)))

    elif expr[0] == "(":
        right = expr[1:searchClosingPar(expr)]
        return parseToTree(right, debug)


def searchMinus(expr):
    parenthesisCounter = 0
    for i in range(len(expr) - 1, -1, -1):
        if expr[i] == ")":
            parenthesisCounter += 1
        elif expr[i] == "(":
            parenthesisCounter -= 1
        elif expr[i] == '-' and parenthesisCounter == 0:
            if expr[i - 1] in ("*", "/", "^", "-", "+", "√"):
                continue
            return i
    return -1


def searchPow(expr):
    parenthesisCounter = 0
    for i, char in enumerate(expr):
        if char == "(":
            parenthesisCounter += 1
        elif char == ")":
            parenthesisCounter -= 1
        elif char == "^" and parenthesisCounter == 0:
            return i
    return -1


def searchClosingPar(expr):
    parenthesisCounter = 0
    for i in range(len(expr)):
        c = expr[i]
        if i == 0 and c == '(':
            continue
        if c == "(":
            parenthesisCounter += 1
        elif c == ")":
            parenthesisCounter -= 1
        elif c == ")" and parenthesisCounter == 0:
            return i
    return -1


def searchPlus(expr):
    parenthesisCounter = 0
    for i in range(len(expr) - 1, -1, -1):
        if expr[i] == ")":
            parenthesisCounter += 1
        elif expr[i] == "(":
            parenthesisCounter -= 1
        elif expr[i] == '+' and parenthesisCounter == 0:
            if expr[i - 1] in ("*", "/", "^", "-", "+", "√"):
                continue
            return i
    return -1


def searchDivMul(expr, c):
    parenthesisCounter = 0
    for i in range(len(expr) - 1, -1, -1):
        if expr[i] == ")":
            parenthesisCounter += 1
        elif expr[i] == "(":
            parenthesisCounter -= 1
        elif expr[i] == c and parenthesisCounter == 0:
            return i
    return -1


def searchSqrt(expr):
    parenthesisCounter = 0
    for i in range(len(expr) - 1, -1, -1):
        if expr[i] == ")":
            parenthesisCounter += 1
        elif expr[i] == "(":
            parenthesisCounter -= 1
        elif expr[i] == "√" and parenthesisCounter == 0:
            return i
    return -1


def searchSinCos(expr, char):
    parenthesisCounter = 0
    for i in range(len(expr) - 1, -1, -1):
        if expr[i] == ")":
            parenthesisCounter += 1
        elif expr[i] == "(":
            parenthesisCounter -= 1
        elif expr[i] == char and parenthesisCounter == 0:
            return i
    return -1


sin = "S"
sqrt = "√"

expr = "(cos(60)*2+1)^2"

# "(2*-√(5^2))^(1+1)" #input("Expr: ")# "-5*(3+2)++--+-+3"  # "13*-+(33+-+-+-+1)^13+(+--213)-+5------5-5-1-2-31-23-------+++-+-+++-12-32-34-123-5*13^2+5-5-(-10/(((3*-3+1)))-5*-13+2/(5-2+3*-5/-6)-5/-12*-31/23/234/-51/-23/(123/-3-3934591^2*-12374))^2"

expr = expr.replace("sin", "S").replace("cos", "C").replace(" ", '')
try:
    tree = round(parseToTree(expr, False), 6)

    print("\n")
    print("My answer:  ", tree)
    # print("Real answer:", eval(expr.replace("^", '**')))
except BaseException as e:
    raise e
input("press any key to exit")
