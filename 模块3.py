
from sympy import *
x1 = Symbol('x1')
x2 = Symbol('x2')
x3 = Symbol('x3')
print(solve([2*x1 + 3*x2 - 5*x3 + 10, 4*x1 + 8*x2 - 3*x3 + 19, -6*x1 + x2 + 4*x3 + 11 ], [x1,x2,x3]))