from SearchFuncs import searchChar

def parseToTree(expr: str):
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
        right = expr[idxAdd+1:]
        return parseToTree(left) + parseToTree(right)

    elif idxSub != -1:
        left = expr[:idxSub]
        if idxSub == 0:
            left = "0"
        right = expr[idxSub+1:]
        return parseToTree(left) - parseToTree(right)

    elif idxMul != -1:
        left = expr[:idxMul]
        right = expr[idxMul+1:]

        return parseToTree(left) * parseToTree(right)

    elif idxDiv != -1:
        left = expr[:idxDiv]
        right = expr[idxDiv + 1:]
        return parseToTree(left) / parseToTree(right)

    elif idxPow != -1:
        left = expr[:idxPow]
        right = expr[idxPow + 1:]
        return parseToTree(left) ** parseToTree(right)

    elif expr[0] == "(":
        right = expr[1:-1]  # expr[1:searchClosingPar(expr)]
        return parseToTree(right)

if __name__ == "__main__":
    expr = input("Expr: ")# "-5*(3+2)++--+-+3"  # "13*-+(33+-+-+-+1)^13+(+--213)-+5------5-5-1-2-31-23-------+++-+-+++-12-32-34-123-5*13^2+5-5-(-10/(((3*-3+1)))-5*-13+2/(5-2+3*-5/-6)-5/-12*-31/23/234/-51/-23/(123/-3-3934591^2*-12374))^2"

    try:
        tree = parseToTree(expr.replace(" ", ''))
        # print(searchPow(expr))

        print("\n")
        print("My answer:  ", tree)  # .evaluate())
        print("Real answer:", eval(expr.replace("^", '**')))
    except BaseException as e:
        print(e)
    input("press any key to exit")
