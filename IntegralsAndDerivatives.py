def integrate(a, b, f):
    s = 0
    dx = 0.00000001
    for k in range(int((b-a)//dx)):
        s += f(k*dx)*dx
    return s

def differentiate(f, x):
    h = 0.0000000001
    return (f(x+h)-f(x))/h

def f(x):
    return 3*x**5

"""print(integrate(0, 10, f))
print(differentiate(f, 3))"""