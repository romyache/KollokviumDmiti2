from integers.MUL_ZZ_Z import MUL_ZZ_Z
from integers.TRANS_N_Z import TRANS_N_Z
from integers.ABS_Z_N import ABS_Z_N
from integers.POZ_Z_D import POZ_Z_D
from rationals.RED_Q_Q import RED_Q_Q

# Модуль Q-8: Деление дробей
# Автор: Никита, группа 5387


def DIV_QQ_Q(a: dict, b: dict) -> dict:
    # числитель результата = числитель_a * знаменатель_b
    den_b_z = TRANS_N_Z(b['den'])         # знаменатель b → целое
    new_num = MUL_ZZ_Z(a['num'], den_b_z)

    # знаменатель результата = знаменатель_a * |числитель_b|
    abs_num_b = ABS_Z_N(b['num'])          # |числитель b| → натуральное
    abs_num_b_z = TRANS_N_Z(abs_num_b)    # натуральное → целое
    den_a_z = TRANS_N_Z(a['den'])
    new_den_z = MUL_ZZ_Z(den_a_z, abs_num_b_z)
    new_den = ABS_Z_N(new_den_z)           # целое → натуральное

    # если числитель b был отрицательным — меняем знак числителя результата
    if POZ_Z_D(b['num']) == 1:
        new_num = {
            'sign': 1 if new_num['sign'] == 0 else 0,
            'n': new_num['n'],
            'digits': new_num['digits']
        }

    result = {
        'num': new_num,
        'den': new_den
    }

    # сокращаем результат
    return RED_Q_Q(result)