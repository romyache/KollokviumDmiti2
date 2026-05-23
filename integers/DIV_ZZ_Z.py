from integers.ABS_Z_N import ABS_Z_N
from integers.POZ_Z_D import POZ_Z_D
from natural.DIV_NN_N import DIV_NN_N
from natural.ADD_1N_N import ADD_1N_N


def DIV_ZZ_Z(a: dict, b: dict) -> dict:
    """
    Z-9 DIV_ZZ_Z — частное от деления целого на целое (делитель отличен от нуля).

    Параметры:
        a (dict): делимое целое число
        b (dict): делитель целое число (не ноль)

    Возвращает:
        dict: целое число — неполное частное от деления a на b
              округление всегда в сторону минус бесконечности
    """
    sign_a = POZ_Z_D(a)
    sign_b = POZ_Z_D(b)

    # Делимое равно нулю — результат ноль
    if sign_a == 0:
        return {'sign': 0, 'n': 0, 'digits': [0]}

    abs_a = ABS_Z_N(a)
    abs_b = ABS_Z_N(b)

    # Делим модули
    q = DIV_NN_N(abs_a, abs_b)

    # Знаки одинаковые — результат положительный
    if sign_a == sign_b:
        return {'sign': 0, 'n': q['n'], 'digits': q['digits']}

    # Знаки разные — результат отрицательный
    # Если деление не точное — округляем вниз (добавляем 1 к модулю)
    # Проверяем: a % b != 0, т.е. |a| не делится нацело на |b|
    from natural.MUL_NN_N import MUL_NN_N
    from natural.COM_NN_D import COM_NN_D
    product = MUL_NN_N(q, abs_b)
    if COM_NN_D(product, abs_a) != 0:
        # Остаток не ноль — округляем вниз
        q = ADD_1N_N(q)

    return {'sign': 1, 'n': q['n'], 'digits': q['digits']}