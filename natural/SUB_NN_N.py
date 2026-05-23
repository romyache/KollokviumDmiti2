from natural.helpers import _make

def SUB_NN_N(a, b):
    digits = a['digits'][:]
    borrow = 0  # заём из следующего разряда
    for i in range(len(digits)):
        db = b['digits'][i] if i <= b['n'] else 0
        d = digits[i] - db - borrow
        if d < 0:
            d += 10   # занимаем 10 из следующего разряда
            borrow = 1
        else:
            borrow = 0
        digits[i] = d
    return _make(digits)