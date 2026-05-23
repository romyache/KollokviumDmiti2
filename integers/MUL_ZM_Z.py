def MUL_ZM_Z(z: dict) -> dict:
    """
    Z-3 MUL_ZM_Z — умножение целого числа на (-1).

    Параметры:
        z (dict): целое число в формате {'sign': ..., 'n': ..., 'digits': [...]}

    Возвращает:
        dict: целое число с противоположным знаком
              (ноль остаётся нулём — знак не меняется)
    """
    # Ноль не меняет знак — все цифры равны 0
    if all(d == 0 for d in z['digits']):
        return {
            'sign': 0,
            'n': z['n'],
            'digits': z['digits'][:]
        }

    new_sign = 1 if z['sign'] == 0 else 0
    return {
        'sign': new_sign,
        'n': z['n'],
        'digits': z['digits'][:]
    }