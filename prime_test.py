import numpy
import math
def prime(upto=10000):
    return filter(lambda num: (num % numpy.arange(2,1+int(math.sqrt(num)))).all(), range(2,upto+1))
prime()