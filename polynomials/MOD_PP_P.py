from polynomials.DIV_PP_P import DIV_PP_P
from polynomials.MUL_PP_P import MUL_PP_P
from polynomials.SUB_PP_P import SUB_PP_P

# Модуль P-10: Остаток от деления многочлена на многочлен
# Автор: Никита, группа 5387


def MOD_PP_P(a: dict, b: dict) -> dict:
    # находим частное
    quotient = DIV_PP_P(a, b)

    # умножаем частное обратно на делитель
    product = MUL_PP_P(quotient, b)

    # вычитаем из делимого — получаем остаток
    return SUB_PP_P(a, product)