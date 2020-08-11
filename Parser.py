from SearchFuncs import searchChar


def calc(expr: str):
    try:
        return float(expr)
    except ValueError:
        pass

    idxAdd = searchChar(expr, "+")
    idxSub = searchChar(expr, "-")
    idxMul = searchChar(expr, "*")
    idxDiv = searchChar(expr, "/")
    idxPow = searchChar(expr, "^")

    if idxAdd != -1:
        left = expr[:idxAdd]
        if idxAdd == 0:
            left = "0"
        right = expr[idxAdd + 1 :]
        return calc(left) + calc(right)

    elif idxSub != -1:
        left = expr[:idxSub]
        if idxSub == 0:
            left = "0"
        right = expr[idxSub + 1 :]
        return calc(left) - calc(right)

    elif idxMul != -1:
        left = expr[:idxMul]
        right = expr[idxMul + 1 :]

        return calc(left) * calc(right)

    elif idxDiv != -1:
        left = expr[:idxDiv]
        right = expr[idxDiv + 1 :]
        return calc(left) / calc(right)

    elif idxPow != -1:
        left = expr[:idxPow]
        right = expr[idxPow + 1 :]
        return calc(left) ** calc(right)

    elif expr[0] == "(":
        right = expr[1:-1]
        return calc(right)


expr = "-5*(3+2)^100"
tree = calc(expr.replace(" ", ""))
print("My answer:  ", tree)
