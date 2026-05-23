from rationals.ADD_QQ_Q import ADD_QQ_Q


def ADD_PP_P(a: dict, b: dict) -> dict:
    """
    P-1 ADD_PP_P — сложение многочленов.

    Параметры:
        a (dict): первый многочлен {'m': ..., 'coeffs': [...]}
        b (dict): второй многочлен {'m': ..., 'coeffs': [...]}

    Возвращает:
        dict: многочлен a + b
    """
    max_deg = max(a['m'], b['m'])
    coeffs = []

    for i in range(max_deg + 1):
        # Берём коэффициент из a или ноль если степень больше
        ca = a['coeffs'][i] if i <= a['m'] else {'num': {'sign': 0, 'n': 0, 'digits': [0]}, 'den': {'n': 0, 'digits': [1]}}
        cb = b['coeffs'][i] if i <= b['m'] else {'num': {'sign': 0, 'n': 0, 'digits': [0]}, 'den': {'n': 0, 'digits': [1]}}
        coeffs.append(ADD_QQ_Q(ca, cb))

    # Убираем старшие нулевые коэффициенты
    while len(coeffs) > 1:
        c = coeffs[-1]
        if all(d == 0 for d in c['num']['digits']):
            coeffs.pop()
        else:
            break

    return {'m': len(coeffs) - 1, 'coeffs': coeffs}