from natural.LCM_NN_N import LCM_NN_N
from natural.DIV_NN_N import DIV_NN_N
from integers.MUL_ZZ_Z import MUL_ZZ_Z
from integers.ADD_ZZ_Z import ADD_ZZ_Z
from integers.TRANS_N_Z import TRANS_N_Z
from rationals.RED_Q_Q import RED_Q_Q

# Модуль Q-5: Сложение дробей
# Автор: Никита, группа 5387


def ADD_QQ_Q(a: dict, b: dict) -> dict:
    # находим НОК знаменателей
    lcm = LCM_NN_N(a['den'], b['den'])

    # делим НОК на каждый знаменатель — получаем множители для числителей
    factor_a = DIV_NN_N(lcm, a['den'])  # lcm / den_a
    factor_b = DIV_NN_N(lcm, b['den'])  # lcm / den_b

    # переводим множители в целые для умножения на числители
    factor_a_z = TRANS_N_Z(factor_a)
    factor_b_z = TRANS_N_Z(factor_b)

    # приводим числители к общему знаменателю
    new_num_a = MUL_ZZ_Z(a['num'], factor_a_z)
    new_num_b = MUL_ZZ_Z(b['num'], factor_b_z)

    # складываем числители
    new_num = ADD_ZZ_Z(new_num_a, new_num_b)

    result = {
        'num': new_num,
        'den': lcm
    }

    # сокращаем результат
    return RED_Q_Q(result)