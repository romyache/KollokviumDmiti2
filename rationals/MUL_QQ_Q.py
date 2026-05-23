from integers.MUL_ZZ_Z import MUL_ZZ_Z
from integers.TRANS_N_Z import TRANS_N_Z
from integers.TRANS_Z_N import TRANS_Z_N
from integers.ABS_Z_N import ABS_Z_N
from rationals.RED_Q_Q import RED_Q_Q

# Модуль Q-7: Умножение дробей
# Автор: Никита, группа 5387


def MUL_QQ_Q(a: dict, b: dict) -> dict:
    # числитель результата = числитель_a * числитель_b
    new_num = MUL_ZZ_Z(a['num'], b['num'])

    # знаменатель результата = знаменатель_a * знаменатель_b
    # знаменатели натуральные — переводим в целые для умножения
    den_a_z = TRANS_N_Z(a['den'])
    den_b_z = TRANS_N_Z(b['den'])
    new_den_z = MUL_ZZ_Z(den_a_z, den_b_z)

    # переводим знаменатель обратно в натуральное
    new_den = ABS_Z_N(new_den_z)

    result = {
        'num': new_num,
        'den': new_den
    }

    # сокращаем результат
    return RED_Q_Q(result)