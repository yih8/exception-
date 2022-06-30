def sqrt(x):
    if not isinstance(x, (int, float)):
        raise TypeError("x must be numeric")
    elif x < 0:
        raise ValueError("x must be positive")
    c=x**0.5
    return c

try:
    x = sqrt("hello Kugou")
except TypeError as err:
    print("Error: " + str(err))

