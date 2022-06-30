
from sympy import *
x = Symbol('x')
y = Symbol('y')
print(solve([3*x + 4*y - 49, 8*x - y - 14], [x, y]))