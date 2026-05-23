from natural.LCM_NN_N import LCM_NN_N
from natural.DIV_NN_N import DIV_NN_N
from integers.MUL_ZZ_Z import MUL_ZZ_Z
from integers.SUB_ZZ_Z import SUB_ZZ_Z
from integers.TRANS_N_Z import TRANS_N_Z
from rationals.RED_Q_Q import RED_Q_Q

# Модуль Q-6: Вычитание дробей
# Автор: Никита, группа 5387


def SUB_QQ_Q(a: dict, b: dict) -> dict:
    # находим НОК знаменателей
    lcm = LCM_NN_N(a['den'], b['den'])

    # множители для приведения к общему знаменателю
    factor_a = DIV_NN_N(lcm, a['den'])
    factor_b = DIV_NN_N(lcm, b['den'])

    factor_a_z = TRANS_N_Z(factor_a)
    factor_b_z = TRANS_N_Z(factor_b)

    # приводим числители к общему знаменателю
    new_num_a = MUL_ZZ_Z(a['num'], factor_a_z)
    new_num_b = MUL_ZZ_Z(b['num'], factor_b_z)

    # вычитаем числители
    new_num = SUB_ZZ_Z(new_num_a, new_num_b)

    result = {
        'num': new_num,
        'den': lcm
    }

    # сокращаем результат
    return RED_Q_Q(result)