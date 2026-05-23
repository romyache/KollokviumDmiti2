from natural.helpers import _make

def MUL_ND_N(a, d):
    digits = []
    carry = 0
    for i in range(a['n'] + 1):
        p = a['digits'][i] * d + carry
        digits.append(p % 10)
        carry = p // 10
    if carry:
        digits.append(carry)
    return _make(digits)