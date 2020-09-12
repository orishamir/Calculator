from Parser import parseToTree as calc
from SearchFuncs import searchChar
# from Node import Node, Num, Var
# from Visualizer import visualizeExprTree


"""def parseToTree(expr: str, debug=False):
    if "=" in expr:
        return Equation(parseToTree(expr[:expr.find("=")]), parseToTree(expr[expr.find("=")+1:]))
    if debug:
        print(expr)
    if expr.isalpha():
        return Var(expr)
    try:
        return Num(int(expr))
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
        right = expr[1:-1]
        return parseToTree(right, debug)

class Equation:
    def __init__(self, left: Node, right: Node):
        self.left = left
        self.right = right
        self.op = "="

    def is_equal(self):
        return

    def solveFor(self, var: Var):
        return NotImplemented

    # for stuff like self +-*/ ...
    def __add__(self, other):
        newSelf = self.__copy__()
        newSelf.left += other
        newSelf.right += other
        return newSelf

    def __sub__(self, other):
        newSelf = self.__copy__()
        newSelf.left -= other
        newSelf.right -= other
        return newSelf

    def __mul__(self, other):
        newSelf = self.__copy__()
        newSelf.left *= other
        newSelf.right *= other
        return newSelf

    def __truediv__(self, other):
        print(self.left / 5)
        newSelf = self.__copy__()
        newSelf.left = newSelf.left / other
        newSelf.right = newSelf.right / other
        return newSelf

    # for stuff like self += ...
    def __iadd__(self, other):
        return self + other

    def __isub__(self, other):
        return self - other

    def __imul__(self, other):
        return self * other

    def __itruediv__(self, other):
        return self / other

    # for stuff like ... +-*/ self
    def __radd__(self, other):
        return other + self

    def __rsub__(self, other):
        return other - self

    def __rmul__(self, other):
        return other * self

    def __rtruediv__(self, other):
        return other / self

    def __copy__(self):
        return Equation(self.left.__copy__(), self.right.__copy__())"""

def getLeftRight(expr, idx):
    # get left first
    left = expr[:idx]
    idxBeforeLeft = max(searchChar(left, "+"), searchChar(left, "-"))
    idxBeforeLeft = 0 if idxBeforeLeft == -1 else idxBeforeLeft
    left = left[idxBeforeLeft:]
    before = expr[:idxBeforeLeft]

    right = expr[idx+1:]
    idxAfterRight = min(searchChar(right, "+") & 9999, searchChar(right, "-") & 99999)
    idxAfterRight = -len(right) if idxAfterRight == -1 else idxAfterRight
    right = right[:idxAfterRight]
    after = expr[idxAfterRight+idx+1:]
    return before, left, right, after

def perform_inverses(equation: str):
    while not equation.startswith("x="):
        print(equation)
        smol, yemin = equation.split("=")
        yemin = float(yemin)

        idxAdd = searchChar(smol, "+")
        idxSub = searchChar(smol, "-")
        idxMul = searchChar(smol, "*")
        idxDiv = searchChar(smol, "/")

        if idxAdd != -1:
            pre, left, right, post = getLeftRight(smol, idxAdd)
            print("add: ", [pre, left, right, post])
            if not left:
                equation = f"{pre}{right}{post}={yemin}"
            elif 'x' in left and 'x' not in right:
                equation = f"{pre}{left}{post}={yemin-calc(right)}"
            elif 'x' in right and "x" not in left:
                equation = f"{pre}+{right}{post}={yemin-calc(left)}"
            elif 'x' not in left and 'x' not in right:
                equation = f"{pre}+{calc(left)+calc(right)}{post}={yemin}"
            else:
                # this case is for 2x+5x-7=0
                coef1, coef2 = left.replace("x*", '').replace("*x", ''), right.replace("x*", '').replace("*x", '')
                equation = f"{pre}+{calc(coef1)+calc(coef2)}*x{post}={yemin}"

        elif idxSub != -1:
            pre, left, right, post = getLeftRight(smol, idxSub)
            print("sub:", [pre, left, right, post])
            if not left:
                equation = f"{pre}{right}{post}={-yemin}"
            elif 'x' in left and 'x' not in right:
                equation = f"{pre}{left}{post}={yemin+calc(right)}"
            elif 'x' in right and 'x' not in left:
                equation = f"{pre}-{right}{post}={-calc(left)}"
            elif 'x' not in left and 'x' not in right:
                equation = f"{pre}{calc(left)-calc(right)}{post}={yemin}"
            else:
                # this case is for 2x+5x-7=0
                coef1, coef2 = left.replace("x*", '').replace("*x", ''), right.replace("x*", '').replace("*x", '')
                equation = f"{pre}+{calc(coef1) - calc(coef2)}*x{post}={yemin}"

        elif idxMul != -1:
            pre, left, right, post = getLeftRight(smol, idxMul)
            print("mul:", [pre, left, right, post])
            if 'x' in left and "x" not in right:
                equation = f"{pre}{left}{post}={yemin/calc(right)}"
            elif 'x' in right and 'x' not in left:
                equation = f"{pre}{right}{post}={yemin/calc(left)}"
            elif 'x' not in left and 'x' not in right:
                equation = f"{pre}{calc(left)*calc(right)}{post}={yemin}"

        elif idxDiv != -1:
            pre, left, right, post = getLeftRight(smol, idxDiv)
            if 'x' in left and "x" not in right:
                equation = f"{pre}{left}{post}={yemin * calc(right)}"
            elif 'x' in right and 'x' not in left:
                # this is something like 3/x. fuck me
                # lets hope x is not 0 ^^
                raise ValueError("no.")
                #equation = f"{pre}{right}{post}={yemin*(1/calc(left))}"
            elif 'x' not in left and 'x' not in right:
                equation = f"{pre}{calc(left) / calc(right)}{post}={yemin}"
    return equation

equation = "135+3*x+3-4*x=0"  # "--5*x+12*x+13-15-2-3*x-5-4+13*x=0"

res = perform_inverses(equation)
print("\n\n\n"); print(res)
