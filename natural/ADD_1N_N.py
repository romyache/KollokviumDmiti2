from natural.helpers import _make

def ADD_1N_N(a):
    digits = a['digits'][:]  # копируем, чтобы не менять оригинал
    carry = 1
    for i in range(len(digits)):
        s = digits[i] + carry
        digits[i] = s % 10
        carry = s // 10
        if carry == 0:
            break  # перенос поглощён — дальше цифры не меняются
    if carry:
        digits.append(carry)  # число выросло на разряд: 999 → 1000
    return _make(digits)