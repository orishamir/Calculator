from CalculationTree import Node, Num

def parseToTree(expr: str, debug):
    if debug:
        print(expr)
    try:
        return Num(float(expr))
    except ValueError:
        pass

    idxAdd = searchPlus(expr)
    idxSub = searchMinus(expr)
    idxMul = searchDivMul(expr, '*')
    idxDiv = searchDivMul(expr, '/')
    idxPow = searchPow(expr)

    if idxAdd != -1:
        left = expr[:idxAdd]
        if idxAdd == 0:
            left = "0"
        right = expr[idxAdd+1:]
        return Node("+", parseToTree(left, debug), parseToTree(right, debug))

    elif idxSub != -1:
        left = expr[:idxSub]
        if idxSub == 0:
            left = "0"
        right = expr[idxSub+1:]
        return Node("-", parseToTree(left, debug), parseToTree(right, debug))

    elif idxMul != -1:
        left = expr[:idxMul]
        right = expr[idxMul+1:]

        return Node("*", parseToTree(left, debug), parseToTree(right, debug))

    elif idxDiv != -1:
        left = expr[:idxDiv]
        right = expr[idxDiv + 1:]
        return Node("/", parseToTree(left, debug), parseToTree(right, debug))

    elif idxPow != -1:
        left = expr[:idxPow]
        right = expr[idxPow + 1:]
        return Node("^", parseToTree(left, debug), parseToTree(right, debug))

    elif expr[0] == "(":
        left = Num(0)
        right = expr[1:searchClosingPar(expr)]
        return parseToTree(right, debug)  # Node('+', left, parseToTree(right, debug))
        # treat (5-3) as +
        #              0   8


def searchMinus(expr):
    parenthesisCounter = 0
    for i in range(len(expr)-1, -1, -1):
        if expr[i] == ")":
            parenthesisCounter += 1
        elif expr[i] == "(":
            parenthesisCounter -= 1
        elif expr[i] == '-' and parenthesisCounter == 0:
            if expr[i-1] in ("*", "/", "^", "-", "+"):
                continue
            return i
    # (1) take for example -10/5+10 or -15/5-10. we should not consider the first '-' as operator.
    # but in the example -(5+2) we do need to.
    if searchPlus(expr) == -1:  # (and no '-' in our expression as well)
        print(expr)
        if len(expr) > 0 and expr[0] == "-":
            return 0
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
    for i in range(len(expr)-1, -1, -1):
        if expr[i] == ")":
            parenthesisCounter += 1
        elif expr[i] == "(":
            parenthesisCounter -= 1
        elif expr[i] == '+' and parenthesisCounter == 0:
            if expr[i-1] in ("*", "/", "^", "-", "+"):
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


if __name__ == '__main__':
    expr = "13*-+(33+-+-+-+1)^13+(+--213)-+5------5-5-1-2-31-23-------+++-+-+++-12-32-34-123-5*13^2+5-5-(-10/(((3*-3+1)))-5*-13+2/(5-2+3*-5/-6)-5/-12*-31/23/234/-51/-23/(123/-3-3934591^2*-12374))^2"

    tree = parseToTree(expr.replace(" ", ''), False)

    print("\n\n")
    print(searchPow(expr))

    print("\n")
    print("My answer:  ", tree.evaluate())
    print("Real answer:", eval(expr.replace("^", '**')))
    input("press any key to exit...")