
#Peter J. Mangelsdorf

#Test for gInt.py


#Imports
from unittest import Testcase
import gInt
import random

#Main
def main():

    #List of gInts to Test.
    gInts = [gInt(3,2), gInt(-8,3), gInt(5,2), gInt(0,1), gInt(1,0)]

    #Lists of Expected Values.
    gAdds = [gInt(3,2), gInt(-8,3), gInt(5,2), gInt(0,1), gInt(1,0)]
    gMuls = [gInt(3,2), gInt(-8,3), gInt(5,2), gInt(0,1), gInt(1,0)]
    gNorms = [gInt(3,2), gInt(-8,3), gInt(5,2), gInt(0,1), gInt(1,0)]

    #__add__ testing
    countdown = 10
    while(countdown != 0):
        n = randrange(0,4,1)
        test_add(gInt[n],gInt[n + 1],gAdds[n])
        countdown -= 1

    #__mul__ testing
    countdown = 10
    while(countdown != 0):
        n = randrange(0,4,1)
        test_mul(gInt[n],gInt[n + 1],gMuls[n])
        countdown -= 1

    #norm testing
    countdown = 5
    while(countdown != 0):
        test_norm(gInt[countdown - 1], gNorms[countdown - 1])
        countdown -= 1


def test_add(gInt1, gInt2, expected):
    actual = gInt1 + gInt2
    assert(actual == expected)
    return

def test_mul(gInt1, gInt2, expected):
    actual = gInt1 * gInt2
    assert(actual == expected)):
    return

def test_norm(gInt, expected):
    actual = norm(gInt)
    assert(actual == expected)):
    return

if __name__ == "__main__":
    main()
