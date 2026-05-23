def TRANS_Z_N(z: dict) -> dict:
    """
    Z-5 TRANS_Z_N — преобразование целого неотрицательного числа в натуральное.

    Параметры:
        z (dict): целое число с sign == 0 (неотрицательное)

    Возвращает:
        dict: натуральное число {'n': ..., 'digits': [...]}

    Исключение:
        ValueError — если передано отрицательное число
    """
    if z['sign'] == 1 and not all(d == 0 for d in z['digits']):
        raise ValueError("TRANS_Z_N: нельзя преобразовать отрицательное целое в натуральное")

    return {
        'n': z['n'],
        'digits': z['digits'][:]
    }