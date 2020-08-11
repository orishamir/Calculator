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

    def evaluate(self):
        left = self.left.evaluate()
        right = self.right.evaluate()

        if self.op == "+":
            return left + right

        if self.op == "-":
            return left - right

        if self.op == "*":
            return left * right

        if self.op == "/":
            return left / right

        if self.op in ("**", "^"):
            return left ** right

        if self.op == "√":
            return _sqrt(right)

class Num:
    def __init__(self, val):
        self.val = val

    def evaluate(self):
        return self.val


def main():
    tree = Node("*", 3, Node("+", 5, 3))
    print(tree.evaluate())

if __name__ == '__main__':
    main()
