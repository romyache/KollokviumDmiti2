from natural.helpers import _make
from natural.MUL_ND_N import MUL_ND_N
from natural.SUB_NN_N import SUB_NN_N

def SUB_NDN_N(a, b, d):
    # вычитаем из a число b умноженное на цифру d
    bd = MUL_ND_N(b, d)
    return SUB_NN_N(a, bd)