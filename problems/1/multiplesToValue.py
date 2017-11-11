"""This module can compute the sum of all multiples of a certain set
of numbers upto a limit. It takes care of intersections so no number
is counted twice :)"""
from math import gcd
import sys
#from functools import reduce


def lcm(a, b):
    """Least common multiple is not in standard libraries?
    It's in gmpy, but this is simple enough."""
    return (a * b) // gcd(a, b)
def sign(x) -> int:
    """Returns -1 if a number is negative and +1 if it is positive."""
    return (x > 0) - (x < 0)

def multiplesToValue(x, V):
    """The Sum of all multiples of x upto and including value V"""
    floor = V//x
    return x * (floor * (floor + 1)) // 2

def compositeMultiplesToValue(listX, V):
    """The Sum of all multiples of all numbers in listX
    upto and including value V"""
    divSet = DivisorSet(listX)
    return divSet.evaluate(V)

class DivisorSet:
    """A composite set of divisors."""
    def __init__(self, divisor=1):
        """Initializer. Inductively created set of LCMs that can evaluate
        multiplesToValue for a set of divisors."""
        self.LCMSet = []
        self.divSet = []
        self.divSet.append(divisor)

        if isinstance(divisor, int):
            self.add(divisor)
        elif isinstance(divisor, list):
            for d in divisor:
                self.add(d)
        else:
            raise AttributeError("Weird Item"+str(divisor))

    def add(self, divisor: int = 1):
        """Add an item to the DivisorSet"""
        self.divSet.append(divisor)
        LCMSet2 = self.LCMSet[:]
        self.LCMSet.append(divisor)
        for x in LCMSet2:
            self.LCMSet.append((-1) * sign(x) * lcm(divisor, abs(x)))

    def evaluate(self, limit: int) -> int:
        """evaluate multiplesToValue for the DivisorSet against a limit"""
        result = 0
        for x in self.LCMSet:
            result += sign(x) * multiplesToValue(abs(x), limit)
        return result

    def list(self):
        """List out internal data structures."""
        print(str(self.divSet)+"\n")
        print(str(self.LCMSet))

def main():
    """Execute the problem."""
    print(compositeMultiplesToValue([3, 5], 999))

if __name__ == "__main__":
    if 'isNullRun' in globals():
        True
    else:
        main()
    