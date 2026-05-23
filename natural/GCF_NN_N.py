from natural.MOD_NN_N import MOD_NN_N
from natural.NZER_N_B import NZER_N_B

def GCF_NN_N(a, b):
    # алгоритм Евклида: пока b != 0, меняем a=b, b=a%b
    while not NZER_N_B(b):
        a, b = b, MOD_NN_N(a, b)
    return a