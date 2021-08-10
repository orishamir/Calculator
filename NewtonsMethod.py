from CalculatorExtended import calc


def apply_method(equ: str):
    l, r = equ.split('=')
    expr = f"{l}-{r}"
    print(expr)

    x0 = 0.5
    try:
        for _ in range(100):
            x0 = x0-calc(expr.replace("x", str(x0)))/differentiate(expr, x0)
    except ValueError:
        print("\nProbably bad x0. this is the furthest I got:")
    return x0

def differentiate(expr, x):
    h = 0.0000000001
    return (calc(expr.replace("x", f"{x+h}"))-calc(expr.replace("x", f"{x}")))/h

print(apply_method("4*l(27*x,9)=(2*l(9,27*x))^2"))
