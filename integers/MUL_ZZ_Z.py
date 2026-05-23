from integers.POZ_Z_D import POZ_Z_D
from integers.ABS_Z_N import ABS_Z_N
from natural.MUL_NN_N import MUL_NN_N
from integers.MUL_ZM_Z import MUL_ZM_Z


def MUL_ZZ_Z(a: dict, b: dict) -> dict:
    """
    Z-8 MUL_ZZ_Z — умножение целых чисел.

    Параметры:
        a (dict): первое целое число
        b (dict): второе целое число

    Возвращает:
        dict: целое число a * b
    """
    sign_a = POZ_Z_D(a)
    sign_b = POZ_Z_D(b)

    # Один из множителей ноль — результат ноль
    if sign_a == 0 or sign_b == 0:
        return {'sign': 0, 'n': 0, 'digits': [0]}

    # Перемножаем модули
    abs_a = ABS_Z_N(a)
    abs_b = ABS_Z_N(b)
    result_digits = MUL_NN_N(abs_a, abs_b)

    # Знак: одинаковые знаки → плюс, разные → минус
    result_sign = 0 if sign_a == sign_b else 1

    return {
        'sign': result_sign,
        'n': result_digits['n'],
        'digits': result_digits['digits']
    }