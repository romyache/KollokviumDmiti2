def _make(digits):
    while len(digits) > 1 and digits[-1] == 0:
        digits.pop()
    return {'n': len(digits) - 1, 'digits': digits}

def from_int(x):
    if x == 0:
        return _make([0])
    digits = []
    while x > 0:
        digits.append(x % 10)
        x //= 10
    return _make(digits)

def to_int(a):
    result = 0
    for i in range(a['n'], -1, -1):
        result = result * 10 + a['digits'][i]
    return result

def to_str(a):
    return ''.join(str(a['digits'][i]) for i in range(a['n'], -1, -1))