from natural.helpers import _make

# Модуль P-6: Степень многочлена
# Автор: Никита, группа 5387


def DEG_P_N(p):
    degree = p['m']

    # если степень 0 — возвращаем натуральное 0
    if degree == 0:
        return _make([0])

    # разбиваем степень на цифры от младшей к старшей
    digits = []
    temp = degree
    while temp > 0:
        digits.append(temp % 10)  # берём последнюю цифру (младшую)
        temp //= 10

    return _make(digits)