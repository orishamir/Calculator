from math import floor, ceil
from SearchFuncs import isClosingAbs, keywords, non_keywords, searchChar


def approximate(num):
    p = 15
    left = [floor(num), 1]
    right = [ceil(num), 1]

    num = round(num, p)

    for i in range(3000):
        mid = [left[0]+right[0], left[1]+right[1]]
        midVal = round(mid[0]/mid[1], p)  # we are not lazy, its to avoid floating point precision errors
        if num < midVal:
            right = mid
        elif num > midVal:
            left = mid
        else:
            return mid
    return

def toExpr(expr):
    for i in range(1, len(expr)-1):
        left, c, right = expr[i-1], expr[i], expr[i+1]
        if c == '(':
            if left in non_keywords:
                return toExpr(f"{expr[:i]}*{expr[i:]}")
        elif c == ')':
            if right in non_keywords:
                return toExpr(f"{expr[:i+1]}*{expr[i+1:]}")
        elif c.isalpha():
            if left in non_keywords:
                return toExpr(f"{expr[:i]}*{expr[i:]}")
            if right in non_keywords:
                return toExpr(f"{expr[:i+1]}*{expr[i+1:]}")
        elif c == '|':
            if isClosingAbs(expr, i):
                if right in non_keywords:
                    return toExpr(f"{expr[:i+1]}*{expr[i+1:]}")
            else:
                if left in non_keywords:
                    return toExpr(f"{expr[:i]}*{expr[i:]}")
    return expr


roots = {str(i): i**0.5 for i in range(2, 99+1) if i**0.5 % 1 != 0}

def isDivable(a, by):
    return round(a/by, 5) % 1 == 0

def toRootRepr(num: float):
    for rt in roots:
        for add in range(-100, 100):
            # check for mul
            for mul in range(-20, 30):
                if mul == 0:
                    continue
                if round((num - add)/mul, 4) == round(roots[rt], 4):
                    res = ""
                    if add != 0:
                        res += str(add)
                    if mul > 0 and add != 0:
                        res += "+"
                    if mul != 1:
                        res += str(mul)
                    res += "√"
                    res += rt
                    return res
            for div in range(-20, 30):
                if div == 0:
                    continue
                if round((num-add)*div, 4) == round(roots[rt], 4):
                    res = ""
                    if add != 0:
                        res += str(add)
                    if div > 0 and add != 0:
                        res += "+"
                    elif div < 0:
                        res += '-'
                    res += "√"
                    res += rt
                    if div != 1:
                        res += '/'
                        res += str(abs(div))
                    return res

def doesContainVar(expr):
    return any(c in expr for c in "abcdefgxyzjk")

from CalculatorExtended import calc

def addThem(arr1, arr2):
    ret = [0 for _ in range(max(len(arr1), len(arr2)))]

    for i in range(max(len(arr1), len(arr2))):
        if i > len(arr1)-1:
            ret[i] = arr2[i]
        elif i > len(arr2)-1:
            ret[i] = arr1[i]
        else:
            ret[i] = arr1[i]+arr2[i]

    return ret


def subThem(arr1, arr2):
    ret = [0 for _ in range(max(len(arr1), len(arr2)))]

    for i in range(max(len(arr1), len(arr2))):
        if i > len(arr1) - 1:
            ret[i] = arr2[i]
        elif i > len(arr2) - 1:
            ret[i] = arr1[i]
        else:
            ret[i] = arr1[i] - arr2[i]

    return ret

def mulThem(arr1, arr2):
    ret = [0 for _ in range(max(len(arr1), len(arr2)))]

    for i in range(max(len(arr1), len(arr2))):
        if i > len(arr1) - 1:
            ret[i] = arr2[i]
        elif i > len(arr2) - 1:
            ret[i] = arr1[i]
        else:
            ret[i] = arr1[i] * arr2[i]

    return ret

def countXpowers(expr, var='x'):
    if expr.isalpha():
        return [0, 1]
    try:
        return [float(expr)]
    except ValueError:
        pass
    idxAdd = searchChar(expr, '+')
    idxSub = searchChar(expr, '-')
    idxMul = searchChar(expr, '*')
    idxDiv = searchChar(expr, '/')
    idxPow = searchChar(expr, '^')

    if idxAdd != -1:
        left = expr[:idxAdd]
        if idxAdd == 0:
            left = "0"
        right = expr[idxAdd + 1:]
        return addThem(countXpowers(left), countXpowers(right))

    elif idxSub > 0:
        left = expr[:idxSub]
        right = expr[idxSub+1:]
        return subThem(countXpowers(left), countXpowers(right))

    elif idxMul != -1:
        left = expr[:idxMul]
        right = expr[idxMul+1:]

        if not doesContainVar(left) and doesContainVar(right):
            try:
                power = int(calc(right.split("^")[1]))
                if power == 0:
                    return []
                return [0]*power+[calc(left)*calc(f"{right[:right.index('x')]}1")]
            except:
                return [0, calc(left)]
        elif doesContainVar(left) and not doesContainVar(right):
            try:
                power = int(calc(left.split("^")[1]))
                if power == 0:
                    return []
                return [0] * power + [calc(right) * calc(f"{left[:left.index('x')]}1")]
            except Exception as e:
                powsRight = countXpowers(right)
                powsLeft = countXpowers(left)

                for i in range(len(powsLeft)):
                    if powsLeft[i] > 0:
                        break
                a = [0] * i + powsRight
                b = powsLeft
                return mulThem(a, b)

        elif doesContainVar(left) and doesContainVar(right):
            powsLeft = countXpowers(left)

            c1 = calc(left.replace("x", '0'))
            c2 = calc(right.replace("x", '0'))
            powsRight = countXpowers(right)

            for i in range(len(powsRight)):
                if powsRight[i] > 0:
                    break
            a = [0]*i + powsLeft
            b = powsRight
            return mulThem(a, b)
        else:
            return 0

    elif idxDiv != -1:
        left = expr[:idxDiv]
        right = expr[idxDiv+1:]

        if not right.isalpha() and left.isalpha():
            return 1/calc(right)
        else:
            return 0

    elif idxPow != -1:
        left, right = expr[:idxPow], expr[idxPow+1:]
        return [0] * (int(calc(right))) + [calc(f"{left[:-1]}1")]

    elif expr[0] == '(':
        return countXpowers(expr[1:-1])

# print(countXpowers("x^3-5*x"))
from math import pi
print(approximate(pi))
