from src import math_lib

def isTabNone():
    digits = None
    assert digits is None, "Test: lista None"
    result = math_lib.max_tab(digits)
    print(result)


def isTabBlank():
    digits = []
    assert digits == [], "Test: lista pusta"
    result = math_lib.max_tab(digits)
    print(result)


def tabWith1Elem():
    digits = [5]
    assert len(digits) >= 0, "Lista 1 elem"
    result = math_lib.max_tab(digits)
    print(result)


def tabWithElems():
    digits = [-4, 3, 0, 37, -15, 7, 3, 32]
    assert len(digits) >= 0, "Lista kilku elem"
    result = math_lib.max_tab(digits)
    print(result)


def negativeNumber():
    digit = -3
    assert digit < 0, "Test: liczba ujemna"
    print(math_lib.is_perfect(digit))


def decimalNumber():
    digit = 2.5
    assert digit % 10 != 0, "Test: liczba dziesiętna"
    print(math_lib.is_perfect(digit))

def NaturalNotPerfect():
    digit = 7
    assert digit > 0, "Test: liczba naturalna, nie perfekcyjna"
    print(math_lib.is_perfect(digit))

def NaturalPerfect():
    digit = 6
    assert digit > 0, "Test: liczba naturalna, perfekcyjna"
    print(math_lib.is_perfect(digit))


if __name__ == "__main__":
    isTabNone()
    isTabBlank()
    tabWith1Elem()
    tabWithElems()
    negativeNumber()
    decimalNumber()
    NaturalNotPerfect()
    NaturalPerfect()
