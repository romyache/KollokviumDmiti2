from natural.DIV_NN_N import DIV_NN_N
from natural.MUL_NN_N import MUL_NN_N
from natural.SUB_NN_N import SUB_NN_N

def MOD_NN_N(a, b):
    q = DIV_NN_N(a, b)
    qb = MUL_NN_N(q, b)
    return SUB_NN_N(a, qb)