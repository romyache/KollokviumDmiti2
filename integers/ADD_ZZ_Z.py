def ADD_ZZ_Z(a: dict, b: dict) -> dict:
    """
    Z-6 ADD_ZZ_Z — сложение целых чисел.

    Параметры:
        a (dict): первое целое число
        b (dict): второе целое число

    Возвращает:
        dict: целое число a + b
    """
    sign_a = POZ_Z_D(a)
    sign_b = POZ_Z_D(b)

    # Один из операндов равен нулю
    if sign_a == 0:
        return b.copy()
    if sign_b == 0:
        return a.copy()

    abs_a = ABS_Z_N(a)
    abs_b = ABS_Z_N(b)

    # Знаки одинаковые — складываем модули, знак сохраняем
    if sign_a == sign_b:
        result_digits = ADD_NN_N(abs_a, abs_b)
        return {
            'sign': a['sign'],
            'n': result_digits['n'],
            'digits': result_digits['digits']
        }

    # Знаки разные — вычитаем меньший модуль из большего
    cmp = COM_NN_D(abs_a, abs_b)

    if cmp == 0:
        # Модули равны — результат ноль
        return {'sign': 0, 'n': 0, 'digits': [0]}

    if cmp == 2:
        # |a| > |b| — результат имеет знак a
        result_digits = SUB_NN_N(abs_a, abs_b)
        return {
            'sign': a['sign'],
            'n': result_digits['n'],
            'digits': result_digits['digits']
        }
    else:
        # |b| > |a| — результат имеет знак b
        result_digits = SUB_NN_N(abs_b, abs_a)
        return {
            'sign': b['sign'],
            'n': result_digits['n'],
            'digits': result_digits['digits']
        }