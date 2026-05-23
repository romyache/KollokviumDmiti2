from rationals.SUB_QQ_Q import SUB_QQ_Q


def SUB_PP_P(a: dict, b: dict) -> dict:
    """
    P-2 SUB_PP_P — вычитание многочленов.

    Параметры:
        a (dict): уменьшаемый многочлен {'m': ..., 'coeffs': [...]}
        b (dict): вычитаемый многочлен {'m': ..., 'coeffs': [...]}

    Возвращает:
        dict: многочлен a - b
    """
    max_deg = max(a['m'], b['m'])
    coeffs = []

    for i in range(max_deg + 1):
        ca = a['coeffs'][i] if i <= a['m'] else {'num': {'sign': 0, 'n': 0, 'digits': [0]}, 'den': {'n': 0, 'digits': [1]}}
        cb = b['coeffs'][i] if i <= b['m'] else {'num': {'sign': 0, 'n': 0, 'digits': [0]}, 'den': {'n': 0, 'digits': [1]}}
        coeffs.append(SUB_QQ_Q(ca, cb))

    # Убираем старшие нулевые коэффициенты
    while len(coeffs) > 1:
        c = coeffs[-1]
        if all(d == 0 for d in c['num']['digits']):
            coeffs.pop()
        else:
            break

    return {'m': len(coeffs) - 1, 'coeffs': coeffs}