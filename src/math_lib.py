def max_tab(digits):
    if digits is None:
        print("Tablica nie może być None")
        return None
    if not digits:  # sprawdza, czy lista jest pusta
        print("Tablica nie powinna być pusta")
        return None

    max_d = digits[0]
    for d in digits:
        if d > max_d:
            max_d = d
    return max_d


def is_perfect(digit):
    if digit < 0:
        return False
    suma = 1
    k = 2
    while k*k < digit:
        if digit % k == 0:
            suma += k + digit/k
        k += 1
    if k*k == digit:
        suma += k

    return suma == digit
