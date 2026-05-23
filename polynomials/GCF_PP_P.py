from polynomials.DEG_P_N import DEG_P_N
from polynomials.MOD_PP_P import MOD_PP_P

# Модуль P-11: НОД многочленов
# Автор: Никита, группа 5387


def _is_zero_poly(p: dict) -> bool:
    return all(all(d == 0 for d in c['num']['digits']) for c in p['coeffs'])


def GCF_PP_P(a: dict, b: dict) -> dict:
    # алгоритм Евклида: пока b не нулевой многочлен
    while not _is_zero_poly(b):
        a, b = b, MOD_PP_P(a, b)
    return a