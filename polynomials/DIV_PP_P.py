from polynomials.DEG_P_N import DEG_P_N
from polynomials.LED_P_Q import LED_P_Q
from polynomials.MUL_Pxk_P import MUL_Pxk_P
from polynomials.SUB_PP_P import SUB_PP_P
from polynomials.ADD_PP_P import ADD_PP_P
from rationals.DIV_QQ_Q import DIV_QQ_Q
from rationals.MUL_QQ_Q import MUL_QQ_Q

# Модуль P-9: Частное от деления многочлена на многочлен
# Автор: Никита, группа 5387


# вспомогательная функция: умножение всех коэффициентов многочлена на рациональное число
def _mul_poly_by_q(p: dict, q: dict) -> dict:
    new_coeffs = [MUL_QQ_Q(c, q) for c in p['coeffs']]
    return {'m': p['m'], 'coeffs': new_coeffs}


def DIV_PP_P(a: dict, b: dict) -> dict:
    # степень делимого и делителя как обычные int (используем p['m'] напрямую)
    deg_a = a['m']
    deg_b = b['m']

    # если степень делимого меньше степени делителя — частное равно нулю
    if deg_a < deg_b:
        zero_q = {'num': {'sign': 0, 'n': 0, 'digits': [0]}, 'den': {'n': 0, 'digits': [1]}}
        return {'m': 0, 'coeffs': [zero_q]}

    # нулевой рациональный коэффициент — пригодится ниже
    zero_q = {'num': {'sign': 0, 'n': 0, 'digits': [0]}, 'den': {'n': 0, 'digits': [1]}}

    # степень частного
    deg_result = deg_a - deg_b

    # инициализируем коэффициенты частного нулями
    result_coeffs = [zero_q] * (deg_result + 1)

    # текущий остаток — начинаем с делимого
    remainder = {'m': a['m'], 'coeffs': a['coeffs'][:]}

    # пока степень остатка >= степени делителя
    while remainder['m'] >= deg_b:
        # проверяем что старший коэффициент остатка не ноль
        lead_rem = LED_P_Q(remainder)
        if all(d == 0 for d in lead_rem['num']['digits']):
            break

        # делим старший коэффициент остатка на старший коэффициент делителя
        lead_b = LED_P_Q(b)
        coeff = DIV_QQ_Q(lead_rem, lead_b)

        # степень текущего члена частного
        k = remainder['m'] - deg_b

        # сохраняем коэффициент в результат
        result_coeffs[k] = coeff

        # строим одночлен: coeff * x^k
        one_term = {'m': 0, 'coeffs': [coeff]}
        one_term_shifted = MUL_Pxk_P(one_term, k)

        # умножаем делитель на этот одночлен: b * coeff * x^k
        b_multiplied = _mul_poly_by_q(b, coeff)
        b_shifted = MUL_Pxk_P({'m': b_multiplied['m'], 'coeffs': b_multiplied['coeffs']}, k)

        # вычитаем из остатка
        remainder = SUB_PP_P(remainder, b_shifted)

    return {'m': deg_result, 'coeffs': result_coeffs}