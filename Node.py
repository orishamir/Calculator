from __future__ import annotations
from cmath import sqrt as _sqrt
class Node():
    def __init__(self, op, left: Node | int, right: Node | int, oldNodeToCopy: Node=None):
        if oldNodeToCopy:
            self.op = oldNodeToCopy.op
            self.left = oldNodeToCopy.left
            self.right = oldNodeToCopy.right
        else:
            self.op = op
            self.left = left
            self.right = right

    def rotateRight(self):
        return

    def evaluate(self):
        left = self.left.evaluate()
        right = self.right.evaluate()

        if self.op == "+":
            if str in (type(left), type(right)):
                return f"({left})+({right})"
            else:
                return left + right

        if self.op == "-":
            if str in (type(left), type(right)):
                return f"({left})-({right})"
            else:
                return left - right

        if self.op == "*":
            if str in (type(left), type(right)):
                return f"({left})*({right})"
            else:
                return left * right

        if self.op == "/":
            if str in (type(left), type(right)):
                return f"({left})/({right})"
            else:
                return left / right

        if self.op in ("**", "^"):
            return left ** right

        if self.op == "√":
            return _sqrt(right)

    def __str__(self):
        return f"({self.left}{self.op}{self.right})"

    def __add__(self, other):
        # adding a number to a tree means
        # setting the current tree's operator as the +
        # setting the left as the current tree
        newNode = self.__copy__()
        newNode.left = Node(newNode.op, newNode.left, newNode.right)
        newNode.right = Num(other) if type(other) in [float, int] else other
        newNode.op = "+"
        return newNode


    def __sub__(self, other):
        newNode = self.__copy__()
        newNode.left = Node(newNode.op, newNode.left, newNode.right)
        newNode.right = Num(other) if type(other) in [float, int] else other
        newNode.op = "-"
        return newNode

    def __mul__(self, other):
        newNode = self.__copy__()
        newNode.left = Node(newNode.op, newNode.left, newNode.right)
        newNode.right = Num(other) if type(other) in [float, int] else other
        newNode.op = "*"
        return newNode

    def __truediv__(self, other):
        newNode = self.__copy__()
        newNode.left = Node(newNode.op, newNode.left, newNode.right)
        newNode.right = Num(other) if type(other) in [float, int] else other
        newNode.op = "/"
        return newNode

    def __iadd__(self, other):
        return self.__add__(other)

    def __isub__(self, other):
        return self.__sub__(other)

    def __imul__(self, other):
        return self.__mul__(other)

    def __itruediv__(self, other):
        return self.__truediv__(other)

    def __radd__(self, other):
        return other.__add__(self)

    def __rsub__(self, other):
        return other.__sub__(self)

    def __rmul__(self, other):
        return other.__mul__(self)

    def __rdiv__(self, other):
        return other.__div__(self)

    def __copy__(self):
        lft = self.left.__copy__()
        rgt = self.right.__copy__()
        return Node(self.op, lft, rgt)

class Num:
    def __init__(self, val):
        self.val = val

    def evaluate(self):
        return self.val

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return f"{self.val}"

    def __int__(self):
        return round(self.val)

    def __add__(self, other):
        return Node("+", self.__copy__(), other.__copy__())

    def __sub__(self, other):
        return Node("-", self.__copy__(), other.__copy__())

    def __mul__(self, other):
        return Node("*", self.__copy__(), other.__copy__())

    def __truediv__(self, other):
        return Node("/", self.__copy__(), other.__copy__())

    def __iadd__(self, other):
        return self.__add__(other)

    def __isub__(self, other):
        return self.__sub__(other)

    def __imul__(self, other):
        return self.__mul__(other)

    def __itruediv__(self, other):
        return self.__truediv__(other)

    def __copy__(self):
        return Num(self.val)


class Var:
    def __init__(self, name):
        self.op = name

    def evaluate(self):
        return f"{self.op}"

    def __copy__(self):
        return Var(self.op)

    def __str__(self):
        return self.op
