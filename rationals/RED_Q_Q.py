from natural.helpers import _make
from natural.GCF_NN_N import GCF_NN_N
from integers.ABS_Z_N import ABS_Z_N
from integers.DIV_ZZ_Z import DIV_ZZ_Z

# Модуль Q-1: Сокращение дроби
# Автор: Никита, группа 5387


def RED_Q_Q(q: dict) -> dict:
    # берём абсолютное значение числителя для нахождения НОД
    abs_num = ABS_Z_N(q['num'])

    # если числитель ноль — сразу возвращаем 0/1
    if all(d == 0 for d in abs_num['digits']):
        return {
            'num': {'sign': 0, 'n': 0, 'digits': [0]},
            'den': _make([1])
        }

    # НОД |числителя| и знаменателя
    gcd = GCF_NN_N(abs_num, q['den'])

    # делим числитель на НОД
    gcd_as_z = {'sign': 0, 'n': gcd['n'], 'digits': gcd['digits']}
    new_num = DIV_ZZ_Z(q['num'], gcd_as_z)

    # делим знаменатель на НОД
    den_as_z = {'sign': 0, 'n': q['den']['n'], 'digits': q['den']['digits']}
    new_den_z = DIV_ZZ_Z(den_as_z, gcd_as_z)
    new_den = _make(new_den_z['digits'])

    return {
        'num': new_num,
        'den': new_den
    }