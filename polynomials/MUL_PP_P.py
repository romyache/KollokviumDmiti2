from polynomials.MUL_PQ_P import MUL_PQ_P
from polynomials.MUL_Pxk_P import MUL_Pxk_P
from polynomials.ADD_PP_P import ADD_PP_P


def MUL_PP_P(a: dict, b: dict) -> dict:
    """
    P-8 MUL_PP_P — умножение многочленов.

    Параметры:
        a (dict): первый многочлен {'m': ..., 'coeffs': [...]}
        b (dict): второй многочлен {'m': ..., 'coeffs': [...]}

    Возвращает:
        dict: многочлен a * b
    """
    # Нулевой многочлен для накопления результата
    zero_q = {
        'num': {'sign': 0, 'n': 0, 'digits': [0]},
        'den': {'n': 0, 'digits': [1]}
    }
    result = {'m': 0, 'coeffs': [zero_q]}

    # Умножаем a на каждый коэффициент b, сдвигаем на степень и складываем
    for i in range(b['m'] + 1):
        # a * коэффициент b[i]
        term = MUL_PQ_P(a, b['coeffs'][i])
        # сдвигаем на x^i
        term = MUL_Pxk_P(term, i)
        # добавляем к результату
        result = ADD_PP_P(result, term)

    return result