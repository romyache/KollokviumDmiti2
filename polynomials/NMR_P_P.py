from polynomials.GCF_PP_P import GCF_PP_P
from polynomials.DER_P_P import DER_P_P
from polynomials.DIV_PP_P import DIV_PP_P
 
 
def NMR_P_P(p):
    """
    P-13: NMR_P_P
    Преобразование многочлена p — устранение кратных корней.
    Результат: многочлен без кратных корней, с теми же простыми корнями.
    Формула: p / НОД(p, p')  где p' — производная p.
    Зависимости: GCF_PP_P, DER_P_P, DIV_PP_P
    """
    # Находим производную p
    dp = DER_P_P(p)

    # НОД(p, p') содержит все кратные множители
    g = GCF_PP_P(p, dp)

    # Делим p на НОД — остаются только простые корни
    return DIV_PP_P(p, g)