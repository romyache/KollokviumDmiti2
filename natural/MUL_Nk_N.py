from natural.helpers import _make
from natural.NZER_N_B import NZER_N_B

def MUL_Nk_N(a, k):
    if NZER_N_B(a):
        return a  # 0 * 10^k = 0
    # Приписываем k нулей к младшим разрядам
    digits = [0] * k + a['digits'][:]
    return _make(digits)