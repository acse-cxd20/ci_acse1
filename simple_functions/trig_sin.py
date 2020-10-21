from numpy import sqrt
from functools import lru_cache
from simple_functions.functions1 import factorial

__all__ = ['my_sin']

@lru_cache(maxsize=None)  # Note: -> @cache in python >= 3.9
def my_sin(x,n):
    sine = 0
    for i in range(n):
        sine += ((-1)**i)*(x**(2.*i + 1))/(factorial(2.*i + 1.))

    return sine
