from math import ceil, floor
from string import ascii_letters
keywords = {
    '+',
    '-',
    '*',
    '/',
    '!',
    '^',
    's','t','c','r','l','R','S','%'
}

non_keywords = (set(ascii_letters).difference(keywords)) | {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}


def searchChar(expr, char):
    parenthesisCounter = 0
    absCounter = 0
    for i in range(len(expr) - 1, -1, -1):
        if expr[i] == ")":
            parenthesisCounter += 1
        elif expr[i] == "(":
            parenthesisCounter -= 1
        elif expr[i] == "|":
            if isClosingAbs(expr, i):
                absCounter -= 1
            else:
                absCounter += 1
        elif expr[i] == char and parenthesisCounter == 0 and absCounter == 0 and expr[i - 1] not in (
        "*", "/", "^", "-", "+", "√"):
            return i
    return -1


def searchSplittingComma(expr, idxLog):
    logCounter = 0
    parCounter = 0
    for i in range(idxLog + 2, len(expr)):
        if expr[i] == 'l' or expr[i] == 'S':
            logCounter += 1
        elif expr[i] == '(':
            parCounter += 1
        elif expr[i] == ')':
            if parCounter == 1:
                logCounter -= 1
            parCounter -= 1
        elif expr[i] == ',' and logCounter == 0:
            return i
    return -1

def searchSigma(expr):
    parenthesisCounter = 0
    afterMiddle = False
    absCounter = 0
    for i in range(len(expr) - 1, -1, -1):
        if absCounter >= expr.count("|") / 2:
            afterMiddle = True
        if expr[i] == ")":
            parenthesisCounter += 1
        elif expr[i] == "(":
            parenthesisCounter -= 1
        elif expr[i] == "|":
            if afterMiddle:
                absCounter -= 1
            else:
                absCounter += 1
        elif expr[i] == "S" and parenthesisCounter == 0 and absCounter == 0 and expr[i - 1] not in (
        "*", "/", "^", "-", "+", "√"):
            break
    else:
        return -1
    return splitSigma(expr, i)


def splitSigma(expr, idxSum):
    sigmaCounter = 0
    Is = []
    parCounter = 0
    for i in range(idxSum+2, len(expr)-1):
        if len(Is) == 3:
            break
        if expr[i] in ("S", 'l'):
            sigmaCounter += 1
        elif expr[i] == '(':
            parCounter += 1
        elif expr[i] == ')':
            if parCounter == 1:
                sigmaCounter -= 1
            parCounter -= 1
        elif expr[i] == ',' and sigmaCounter == 0:
            Is.append(i)
    a, b = Is

    start, end, func = expr[2:a], expr[a+1:b], expr[b+1:-1]
    var, start = start.split("=")
    return var, start, end, func


def isClosingAbs(expr, i):
    if i == 0:
        return False
    if i == len(expr)-1:
        return True

    left, right = expr[i-1], expr[i+1]
    if right == '|':
        return isClosingAbs(expr, i+1)
    if left == '|':
        return isClosingAbs(expr, i-1)
    if left in non_keywords and right in non_keywords:
        return False
    if right in (keywords.difference({'-', '+'})):
        return True
    if left.isnumeric():
        return True
    return False


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

def searchPlus(expr):
    parenthesisCounter = 0
    for i in range(len(expr)-1, -1, -1):
        if expr[i] == ")":
            parenthesisCounter += 1
        elif expr[i] == "(":
            parenthesisCounter -= 1
        elif expr[i] == '+' and parenthesisCounter == 0:
            if expr[i-1] in ("*", "/", "^", "-", "+", "√", "!"):
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

def searchMinus(expr):
    parenthesisCounter = 0
    for i in range(len(expr)-1, -1, -1):
        if expr[i] == ")":
            parenthesisCounter += 1
        elif expr[i] == "(":
            parenthesisCounter -= 1
        elif expr[i] == '-' and parenthesisCounter == 0:
            if expr[i-1] in ("*", "/", "^", "-", "+", "√", "!"):
                continue
            return i
    return -1