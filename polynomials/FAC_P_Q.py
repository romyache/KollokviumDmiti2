from integers.ABS_Z_N import ABS_Z_N
from integers.TRANS_Z_N import TRANS_Z_N
from integers.TRANS_N_Z import TRANS_N_Z
from integers.DIV_ZZ_Z import DIV_ZZ_Z
from natural.LCM_NN_N import LCM_NN_N
from natural.GCF_NN_N import GCF_NN_N


def FAC_P_Q(p: dict) -> dict:
    """
    P-7 FAC_P_Q — вынесение из многочлена НОК знаменателей коэффициентов и НОД числителей.

    Параметры:
        p (dict): многочлен {'m': ..., 'coeffs': [...]}
                  каждый коэффициент — рациональное число {'num': ..., 'den': ...}

    Возвращает:
        dict: рациональное число — общий множитель {'num': ..., 'den': ...}
              после вынесения этого множителя многочлен становится примитивным
    """
    # Считаем НОК всех знаменателей
    lcm_den = p['coeffs'][0]['den']
    for i in range(1, p['m'] + 1):
        lcm_den = LCM_NN_N(lcm_den, p['coeffs'][i]['den'])

    # Считаем НОД всех числителей (берём модули)
    gcd_num = ABS_Z_N(p['coeffs'][0]['num'])
    for i in range(1, p['m'] + 1):
        gcd_num = GCF_NN_N(gcd_num, ABS_Z_N(p['coeffs'][i]['num']))

    # Результат: числитель = НОД числителей (целое), знаменатель = НОК знаменателей (натуральное)
    return {
        'num': TRANS_N_Z(gcd_num),
        'den': lcm_den
    }