from natural.GCF_NN_N import GCF_NN_N
from natural.LCM_NN_N import LCM_NN_N
from integers.ABS_Z_N import ABS_Z_N
from integers.TRANS_N_Z import TRANS_N_Z
from integers.TRANS_Z_N import TRANS_Z_N
from integers.DIV_ZZ_Z import DIV_ZZ_Z

# Модуль P-7: Вынесение из многочлена НОК знаменателей и НОД числителей коэффициентов
# Автор: Никита, группа 5387


def FAC_P_Q(p: dict) -> dict:
    # собираем числители и знаменатели всех ненулевых коэффициентов
    numerators = []
    denominators = []

    for coeff in p['coeffs']:
        num = coeff['num']
        den = coeff['den']

        # пропускаем нулевые коэффициенты
        if all(d == 0 for d in num['digits']):
            continue

        numerators.append(ABS_Z_N(num))   # |числитель| как натуральное
        denominators.append(den)           # знаменатель (уже натуральное)

    # если все коэффициенты нулевые — возвращаем 0/1
    if not numerators:
        return {
            'num': {'sign': 0, 'n': 0, 'digits': [0]},
            'den': {'n': 0, 'digits': [1]}
        }

    # НОД всех числителей (по модулю)
    gcd_num = numerators[0]
    for num in numerators[1:]:
        gcd_num = GCF_NN_N(gcd_num, num)

    # НОК всех знаменателей
    lcm_den = denominators[0]
    for den in denominators[1:]:
        lcm_den = LCM_NN_N(lcm_den, den)

    # результат: НОД числителей / НОК знаменателей
    # числитель результата — целое положительное (знак 0)
    result_num = TRANS_N_Z(gcd_num)

    return {
        'num': result_num,
        'den': lcm_den
    }