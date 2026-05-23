from natural.MUL_ND_N import MUL_ND_N
from natural.MUL_Nk_N import MUL_Nk_N
from natural.COM_NN_D import COM_NN_D

def DIV_NN_Dk(a, b, k):
    # ищем цифру d от 9 до 0 такую что b*10^k*d <= a
    bk = MUL_Nk_N(b, k)
    for d in range(9, -1, -1):
        t = MUL_ND_N(bk, d)
        if COM_NN_D(t, a) != 2:  # t <= a
            return d
    return 0