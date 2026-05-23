from natural.helpers import _make

# Модуль P-12: Производная многочлена
# Автор: Никита, группа 5387


def DER_P_P(p):
    # производная константы — ноль
    if p['m'] == 0:
        zero_q = {
            'num': {'sign': 0, 'n': 0, 'digits': [0]},
            'den': _make([1])
        }
        return {
            'm': 0,
            'coeffs': [zero_q]
        }

    new_coeffs = []

    # проходим по коэффициентам начиная с индекса 1
    # (c0 при дифференцировании исчезает)
    for i in range(1, p['m'] + 1):
        ci = p['coeffs'][i]  # коэффициент при x^i

        # умножаем числитель ci на i напрямую, не вызывая MUL_QQ_Q
        # числитель — целое число, просто умножаем каждую цифру через обычную арифметику
        old_num = ci['num']
        old_digits = old_num['digits']  # цифры от младшей к старшей

        # переводим длинное число в обычный int, умножаем на i, переводим обратно
        value = _digits_to_int(old_digits)
        value = value * i

        new_digits = _int_to_digits(value)
        new_num = {
            'sign': old_num['sign'],  # знак не меняется (i > 0 всегда)
            'n': len(new_digits) - 1,
            'digits': new_digits
        }

        # знаменатель не меняется — умножаем на целое число, знаменатель тот же
        new_coeffs.append({
            'num': new_num,
            'den': ci['den']
        })

    return {
        'm': p['m'] - 1,
        'coeffs': new_coeffs
    }


def _digits_to_int(digits):
    result = 0
    for i in range(len(digits) - 1, -1, -1):
        result = result * 10 + digits[i]
    return result


def _int_to_digits(n):
    if n == 0:
        return [0]
    digits = []
    while n > 0:
        digits.append(n % 10)
        n //= 10
    return digits