from integers.DIV_ZZ_Z import DIV_ZZ_Z
from integers.MUL_ZZ_Z import MUL_ZZ_Z
from integers.SUB_ZZ_Z import SUB_ZZ_Z
from integers.MUL_ZM_Z import MUL_ZM_Z


def MOD_ZZ_Z(a: dict, b: dict) -> dict:
    """
    Z-10 MOD_ZZ_Z — остаток от деления целого на целое (делитель отличен от нуля).

    Параметры:
        a (dict): делимое целое число
        b (dict): делитель целое число (не ноль)

    Возвращает:
        dict: целое число — остаток от деления a на b
              остаток имеет тот же знак что и делитель b
    """
    # a = b * q + r  =>  r = a - b * q
    q = DIV_ZZ_Z(a, b)
    bq = MUL_ZZ_Z(b, q)
    return SUB_ZZ_Z(a, bq)