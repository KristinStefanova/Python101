def GCD(n1, n2):
    result = 10
    while result != 0:
        result = n1 % n2
        n1 = n2
        n2 = result
    return n1


def simplify_fraction(fraction):
    if type(fraction) is not tuple:
        raise TypeError
    nominator, denominator = fraction
    if type(nominator) is not int or type(denominator) is not int:
        raise ValueError
    gcd = GCD(max(nominator, denominator), min(nominator, denominator))
    rem = 2
    while rem <= min(nominator, denominator):
        if nominator % gcd == 0 and denominator % gcd == 0:
            nominator //= gcd
            denominator //= gcd
        rem += 1
    return((nominator, denominator))


def collect_fractions(fractions):
    if type(fractions) is not list:
        raise TypeError
    if any([True for fr in fractions if type(fr) is not tuple]):
        raise ValueError
    return simplify_fraction(
        (fractions[0][0] * fractions[1][1] + fractions[0][1] * fractions[1][0],
            fractions[0][1] * fractions[1][1]))


def sort_fractions(fractions):
    if type(fractions) is not list:
        raise TypeError
    if any([True for fr in fractions if type(fr) is not tuple]):
        raise ValueError
    return sorted(fractions, key=lambda x: (x[0] / x[1]))
