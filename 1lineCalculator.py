def searchChar(expr, char):
    global pc
    pc = 0
    return ([i for i in range(len(expr)-1, -1, -1) if

            (exec("pc += 1", globals()) if expr[i] == ')' else
             exec("pc -= 1", globals()) if expr[i] == '(' else
             True) and
     expr[i] == char and pc == 0 and expr[i-1] not in ("*", "/", "-", "+", "^")] + [-1])[0]


def calc(expr):
    return float(expr) if expr[1:].isnumeric() or len(expr) == 1 else\
        (
        (calc((expr[:idx] if expr[:idx] else "0")) + calc(expr[idx+1:]))  if (idx := searchChar(expr, "+")) != -1 else
        (calc((expr[:idx] if expr[:idx] else "0")) - calc(expr[idx+1:]))  if (idx := searchChar(expr,"-")) != -1 else
        (calc(expr[:idx]) * calc(expr[idx+1:]))                           if (idx := searchChar(expr,"*")) != -1 else
        (calc(expr[:idx]) / calc(expr[idx+1:]))                           if (idx := searchChar(expr,"/")) != -1 else
        calc(expr[1:-1]) if expr[0] == "(" else -1
        )

expr = "13*-+(33+-+-+-+1)+(+--213)-+5------5-5-1-2-31-23-------+++-+-+++-12-32-34-123-5*13+5-5-(-10/(((3*-3+1)))-5*-13+2/(5-2+3*-5/-6)-5/-12*-31/23/234/-51/-23/(123/-3-3934591*-12374))"
print(calc(expr))
print(eval(expr))
