from pprint import pprint
import numpy as np

charT = [
    [1, 1, 1, 1, 1],
    [0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0],
]


def printChar(arr):
    print(f"Size: {len(arr[0])}x{len(arr)}")
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            print('█' if arr[i][j] == 1 else ' ', end='')
        print()

def increaseFont(arr, newFont):
    w, h = len(arr[0]), len(arr)
    result = []
    for i in range(h*newFont):
        result.append([])
        for j in range(w*newFont):
            result[-1].append(0)

    for i in range(len(arr)):
        for j in range(len(arr[i])):
            val = arr[i][j]

            resultI = i*newFont
            resultJ = j*newFont
            for ki in range(newFont):
                for kj in range(newFont):
                    result[resultI+ki][resultJ+kj] = val

            # print(f"({i}, {j}) --> ({resultI}, {resultJ})")
    return result

LEFT = -1
RIGHT = 1
def moveCursor(expr: str, direction: int):
    curpos = expr.index("_")
    left, right = expr[(len(expr)+(curpos-1))%len(expr)], expr[(len(expr)+curpos+1)%len(expr)]

    if direction == LEFT and (left in (',') or expr[curpos-2] in ('$', 's', 'c', 'l', 't')):
        direction *= 2
    elif direction == RIGHT and right in ('$', 's', 'c', 'l', 't') and curpos != len(expr)-1:
        direction *= 2

    curpos = (curpos+direction) % len(expr)
    expr = expr.replace("_", '')
    return f"{expr[:curpos]}_{expr[curpos:]}"

fontsize = 3

print(moveCursor("l(2,8)_", 1))
