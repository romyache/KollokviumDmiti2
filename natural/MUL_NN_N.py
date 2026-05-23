from natural.helpers import _make
from natural.MUL_ND_N import MUL_ND_N
from natural.MUL_Nk_N import MUL_Nk_N
from natural.ADD_NN_N import ADD_NN_N

def MUL_NN_N(a, b):
    # умножаем a на каждую цифру b, сдвигаем и складываем
    result = _make([0])
    for i in range(b['n'] + 1):
        t = MUL_ND_N(a, b['digits'][i])  # a * цифра
        t = MUL_Nk_N(t, i)               # сдвиг на i позиций
        result = ADD_NN_N(result, t)      # прибавляем
    return result