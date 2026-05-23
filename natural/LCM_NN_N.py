from natural.GCF_NN_N import GCF_NN_N
from natural.MUL_NN_N import MUL_NN_N
from natural.DIV_NN_N import DIV_NN_N

def LCM_NN_N(a, b):
    # НОК = a * b / НОД(a, b)
    g = GCF_NN_N(a, b)
    return MUL_NN_N(DIV_NN_N(a, g), b)