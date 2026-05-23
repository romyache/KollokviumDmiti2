from natural.helpers import _make

def ADD_NN_N(a, b):
    len_a = a['n'] + 1
    len_b = b['n'] + 1
    max_len = max(len_a, len_b)
    digits = []
    carry = 0
    for i in range(max_len):
        da = a['digits'][i] if i < len_a else 0
        db = b['digits'][i] if i < len_b else 0
        s = da + db + carry
        digits.append(s % 10)
        carry = s // 10
    if carry:
        digits.append(carry)  # последний перенос: 99 + 1 = 100
    return _make(digits)