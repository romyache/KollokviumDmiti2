from integers.MUL_ZM_Z import MUL_ZM_Z
from integers.ADD_ZZ_Z import ADD_ZZ_Z


def SUB_ZZ_Z(a: dict, b: dict) -> dict:
    """
    Z-7 SUB_ZZ_Z — вычитание целых чисел.

    Параметры:
        a (dict): уменьшаемое целое число
        b (dict): вычитаемое целое число

    Возвращает:
        dict: целое число a - b
    """
    # a - b = a + (-b)
    neg_b = MUL_ZM_Z(b)
    return ADD_ZZ_Z(a, neg_b)