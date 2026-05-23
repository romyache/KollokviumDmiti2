from natural.helpers import _make

# Модуль P-4: Умножение многочлена на x^k, k — натуральное или 0
# Автор: Никита, группа 5387


def MUL_Pxk_P(p, k):
    if k < 0:
        raise ValueError("k должно быть >= 0")

    # рациональный ноль: 0/1
    zero_q = {
        'num': {'sign': 0, 'n': 0, 'digits': [0]},
        'den': _make([1])
    }

    # добавляем k нулей перед существующими коэффициентами
    new_coeffs = [zero_q] * k + p['coeffs']
    new_degree = p['m'] + k

    return {
        'm': new_degree,
        'coeffs': new_coeffs
    }