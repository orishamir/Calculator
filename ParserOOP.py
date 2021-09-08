from SearchFuncs import searchDivMul, searchPow, searchPlus, searchMinus
from Node import Node, Num, Var

def parseToTree(expr: str, debug):
    if debug:
        print(expr)
    if expr.isalpha():
        return Var(expr)
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
        right = expr[1:-1]
        return parseToTree(right, debug)  # Node('+', left, parseToTree(right, debug))


if __name__ == '__main__':
    expr = "(5+2)*3"  # "13*-+(33+-+-+-+1)^13+(+--213)-+5------5-5-1-2-31-23-------+++-+-+++-12-32-34-123-5*13^2+5-5-(-10/(((3*-3+1)))-5*-13+2/(5-2+3*-5/-6)-5/-12*-31/23/234/-51/-23/(123/-3-3934591^2*-12374))^2"

    tree = parseToTree(expr.replace(" ", ''), False)

    print("\n")
    print("My answer:  ", tree)
