from natural.helpers import _make
from natural.DIV_NN_Dk import DIV_NN_Dk
from natural.SUB_NDN_N import SUB_NDN_N
from natural.MUL_Nk_N import MUL_Nk_N

def DIV_NN_N(a, b):
    result = [0] * (a['n'] + 1)
    remainder = a
    for k in range(a['n'], -1, -1):
        d = DIV_NN_Dk(remainder, b, k)
        result[k] = d
        if d > 0:
            bk = MUL_Nk_N(b, k)
            remainder = SUB_NDN_N(remainder, bk, d)
    return _make(result)