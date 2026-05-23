from rationals.MUL_QQ_Q import MUL_QQ_Q


def MUL_PQ_P(p: dict, q: dict) -> dict:
    """
    P-3 MUL_PQ_P — умножение многочлена на рациональное число.

    Параметры:
        p (dict): многочлен {'m': ..., 'coeffs': [...]}
        q (dict): рациональное число {'num': ..., 'den': ...}

    Возвращает:
        dict: многочлен p * q
    """
    # Умножаем каждый коэффициент на q
    coeffs = [MUL_QQ_Q(c, q) for c in p['coeffs']]

    return {'m': p['m'], 'coeffs': coeffs}