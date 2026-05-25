# ui.py
# Пользовательский интерфейс системы компьютерной алгебры.
# Авторы: Никита, Данил, Роман

import sys

# ── Импорты всех модулей ──────────────────────────────────────────────────────
from natural import from_int, to_int, to_str
from natural import (COM_NN_D, NZER_N_B, ADD_1N_N, ADD_NN_N, SUB_NN_N,
                     MUL_ND_N, MUL_Nk_N, MUL_NN_N, SUB_NDN_N,
                     DIV_NN_Dk, DIV_NN_N, MOD_NN_N, GCF_NN_N, LCM_NN_N)
from integers import (ABS_Z_N, POZ_Z_D, MUL_ZM_Z, TRANS_N_Z, TRANS_Z_N,
                      ADD_ZZ_Z, SUB_ZZ_Z, MUL_ZZ_Z, DIV_ZZ_Z, MOD_ZZ_Z)
from rationals import (RED_Q_Q, INT_Q_B, TRANS_Z_Q, TRANS_Q_Z,
                       ADD_QQ_Q, SUB_QQ_Q, MUL_QQ_Q, DIV_QQ_Q)
from polynomials import (ADD_PP_P, SUB_PP_P, MUL_PQ_P, MUL_Pxk_P,
                          LED_P_Q, DEG_P_N, FAC_P_Q, MUL_PP_P,
                          DIV_PP_P, MOD_PP_P, GCF_PP_P, DER_P_P, NMR_P_P)


# ══════════════════════════════════════════════════════════════════════════════
# Вспомогательные функции ввода/вывода
# ══════════════════════════════════════════════════════════════════════════════

def input_natural(prompt):
    """Ввод натурального числа с клавиатуры."""
    while True:
        s = input(prompt).strip()
        if s.isdigit():
            return from_int(int(s))
        print("  Ошибка: введите натуральное число (0 и больше).")


def input_integer(prompt):
    """Ввод целого числа с клавиатуры."""
    while True:
        s = input(prompt).strip()
        try:
            val = int(s)
            n = from_int(abs(val))
            return {'sign': 1 if val < 0 else 0, 'n': n['n'], 'digits': n['digits']}
        except ValueError:
            print("  Ошибка: введите целое число (например: -42 или 17).")


def input_rational(prompt):
    """Ввод рационального числа в формате числитель/знаменатель."""
    print(f"{prompt} (формат: числитель/знаменатель, например 3/4 или -1/2)")
    while True:
        s = input("  > ").strip()
        try:
            if '/' in s:
                parts = s.split('/')
                num = int(parts[0].strip())
                den = int(parts[1].strip())
                if den <= 0:
                    print("  Ошибка: знаменатель должен быть положительным.")
                    continue
            else:
                num = int(s)
                den = 1
            n = from_int(abs(num))
            z_num = {'sign': 1 if num < 0 else 0, 'n': n['n'], 'digits': n['digits']}
            q = {'num': z_num, 'den': from_int(den)}
            return RED_Q_Q(q)
        except (ValueError, IndexError):
            print("  Ошибка: введите число в формате 3/4 или -1/2.")


def input_polynomial(prompt):
    """Ввод многочлена по коэффициентам."""
    print(f"{prompt}")
    while True:
        try:
            deg = int(input("  Степень многочлена: ").strip())
            if deg < 0:
                print("  Ошибка: степень должна быть >= 0.")
                continue
            coeffs = []
            for i in range(deg + 1):
                q = input_rational(f"  Коэффициент при x^{i}")
                coeffs.append(q)
            return {'m': deg, 'coeffs': coeffs}
        except ValueError:
            print("  Ошибка: введите целое число для степени.")


def nat_to_str(a):
    return to_str(a)


def int_to_str(z):
    val = to_int({'n': z['n'], 'digits': z['digits']})
    return f"-{val}" if z['sign'] == 1 and val != 0 else str(val)


def rat_to_str(q):
    num = to_int({'n': q['num']['n'], 'digits': q['num']['digits']})
    if q['num']['sign'] == 1 and num != 0:
        num = -num
    den = to_int(q['den'])
    if den == 1:
        return str(num)
    return f"{num}/{den}"


def poly_to_str(p):
    terms = []
    for i in range(p['m'] + 1):
        c = rat_to_str(p['coeffs'][i])
        # пропускаем нулевые коэффициенты (кроме константного многочлена)
        num_val = to_int({'n': p['coeffs'][i]['num']['n'], 'digits': p['coeffs'][i]['num']['digits']})
        if num_val == 0 and p['m'] > 0:
            continue
        if i == 0:
            terms.append(c)
        elif i == 1:
            terms.append(f"({c})*x")
        else:
            terms.append(f"({c})*x^{i}")
    return " + ".join(terms) if terms else "0"


# ══════════════════════════════════════════════════════════════════════════════
# Меню натуральных чисел
# ══════════════════════════════════════════════════════════════════════════════

def menu_natural():
    ops = {
        '1':  ('Сравнение (COM_NN_D)',           lambda: _nat_compare()),
        '2':  ('Проверка на ноль (NZER_N_B)',     lambda: _nat_is_zero()),
        '3':  ('Прибавить 1 (ADD_1N_N)',          lambda: _nat_add1()),
        '4':  ('Сложение (ADD_NN_N)',             lambda: _nat_bin(ADD_NN_N, '+')),
        '5':  ('Вычитание (SUB_NN_N)',            lambda: _nat_bin(SUB_NN_N, '-')),
        '6':  ('Умножение на цифру (MUL_ND_N)',   lambda: _nat_mul_digit()),
        '7':  ('Умножение на 10^k (MUL_Nk_N)',    lambda: _nat_mul_10k()),
        '8':  ('Умножение (MUL_NN_N)',            lambda: _nat_bin(MUL_NN_N, '*')),
        '9':  ('Деление (DIV_NN_N)',              lambda: _nat_bin(DIV_NN_N, '//')),
        '10': ('Остаток (MOD_NN_N)',              lambda: _nat_bin(MOD_NN_N, 'mod')),
        '11': ('НОД (GCF_NN_N)',                  lambda: _nat_bin(GCF_NN_N, 'НОД')),
        '12': ('НОК (LCM_NN_N)',                  lambda: _nat_bin(LCM_NN_N, 'НОК')),
    }
    _run_menu("НАТУРАЛЬНЫЕ ЧИСЛА", ops)


def _nat_compare():
    a = input_natural("  Первое число: ")
    b = input_natural("  Второе число: ")
    r = COM_NN_D(a, b)
    msg = {2: 'первое > второго', 1: 'первое < второго', 0: 'числа равны'}
    print(f"  Результат: {msg[r]} (код {r})")


def _nat_is_zero():
    a = input_natural("  Число: ")
    print(f"  Результат: {'ноль' if NZER_N_B(a) else 'не ноль'}")


def _nat_add1():
    a = input_natural("  Число: ")
    print(f"  Результат: {nat_to_str(ADD_1N_N(a))}")


def _nat_bin(fn, op):
    a = input_natural("  Первое число: ")
    b = input_natural("  Второе число: ")
    try:
        r = fn(a, b)
        print(f"  {nat_to_str(a)} {op} {nat_to_str(b)} = {nat_to_str(r)}")
    except Exception as e:
        print(f"  Ошибка: {e}")


def _nat_mul_digit():
    a = input_natural("  Число: ")
    while True:
        try:
            d = int(input("  Цифра (0-9): "))
            if 0 <= d <= 9:
                break
            print("  Введите цифру от 0 до 9.")
        except ValueError:
            pass
    print(f"  Результат: {nat_to_str(MUL_ND_N(a, d))}")


def _nat_mul_10k():
    a = input_natural("  Число: ")
    while True:
        try:
            k = int(input("  Показатель k: "))
            if k >= 0:
                break
            print("  k должно быть >= 0.")
        except ValueError:
            pass
    print(f"  Результат: {nat_to_str(MUL_Nk_N(a, k))}")


# ══════════════════════════════════════════════════════════════════════════════
# Меню целых чисел
# ══════════════════════════════════════════════════════════════════════════════

def menu_integers():
    ops = {
        '1': ('Абсолютная величина (ABS_Z_N)',   lambda: _int_abs()),
        '2': ('Знак числа (POZ_Z_D)',             lambda: _int_sign()),
        '3': ('Умножить на -1 (MUL_ZM_Z)',        lambda: _int_neg()),
        '4': ('Сложение (ADD_ZZ_Z)',              lambda: _int_bin(ADD_ZZ_Z, '+')),
        '5': ('Вычитание (SUB_ZZ_Z)',             lambda: _int_bin(SUB_ZZ_Z, '-')),
        '6': ('Умножение (MUL_ZZ_Z)',             lambda: _int_bin(MUL_ZZ_Z, '*')),
        '7': ('Деление (DIV_ZZ_Z)',               lambda: _int_bin(DIV_ZZ_Z, '//')),
        '8': ('Остаток (MOD_ZZ_Z)',               lambda: _int_bin(MOD_ZZ_Z, 'mod')),
    }
    _run_menu("ЦЕЛЫЕ ЧИСЛА", ops)


def _int_abs():
    a = input_integer("  Число: ")
    print(f"  |{int_to_str(a)}| = {nat_to_str(ABS_Z_N(a))}")


def _int_sign():
    a = input_integer("  Число: ")
    r = POZ_Z_D(a)
    msg = {2: 'положительное', 0: 'ноль', 1: 'отрицательное'}
    print(f"  {int_to_str(a)}: {msg[r]} (код {r})")


def _int_neg():
    a = input_integer("  Число: ")
    print(f"  -{int_to_str(a)} = {int_to_str(MUL_ZM_Z(a))}")


def _int_bin(fn, op):
    a = input_integer("  Первое число: ")
    b = input_integer("  Второе число: ")
    try:
        r = fn(a, b)
        print(f"  {int_to_str(a)} {op} {int_to_str(b)} = {int_to_str(r)}")
    except Exception as e:
        print(f"  Ошибка: {e}")


# ══════════════════════════════════════════════════════════════════════════════
# Меню рациональных чисел
# ══════════════════════════════════════════════════════════════════════════════

def menu_rationals():
    ops = {
        '1': ('Сокращение дроби (RED_Q_Q)',         lambda: _rat_reduce()),
        '2': ('Проверка на целое (INT_Q_B)',         lambda: _rat_is_int()),
        '3': ('Сложение (ADD_QQ_Q)',                 lambda: _rat_bin(ADD_QQ_Q, '+')),
        '4': ('Вычитание (SUB_QQ_Q)',                lambda: _rat_bin(SUB_QQ_Q, '-')),
        '5': ('Умножение (MUL_QQ_Q)',                lambda: _rat_bin(MUL_QQ_Q, '*')),
        '6': ('Деление (DIV_QQ_Q)',                  lambda: _rat_bin(DIV_QQ_Q, '/')),
    }
    _run_menu("РАЦИОНАЛЬНЫЕ ЧИСЛА", ops)


def _rat_reduce():
    a = input_rational("  Дробь")
    print(f"  Сокращённая: {rat_to_str(RED_Q_Q(a))}")


def _rat_is_int():
    a = input_rational("  Дробь")
    print(f"  Результат: {'целое' if INT_Q_B(a) else 'не целое'}")


def _rat_bin(fn, op):
    a = input_rational("  Первая дробь")
    b = input_rational("  Вторая дробь")
    try:
        r = fn(a, b)
        print(f"  {rat_to_str(a)} {op} {rat_to_str(b)} = {rat_to_str(r)}")
    except Exception as e:
        print(f"  Ошибка: {e}")


# ══════════════════════════════════════════════════════════════════════════════
# Меню многочленов
# ══════════════════════════════════════════════════════════════════════════════

def menu_polynomials():
    ops = {
        '1':  ('Сложение (ADD_PP_P)',               lambda: _poly_bin(ADD_PP_P, '+')),
        '2':  ('Вычитание (SUB_PP_P)',              lambda: _poly_bin(SUB_PP_P, '-')),
        '3':  ('Умножение (MUL_PP_P)',              lambda: _poly_bin(MUL_PP_P, '*')),
        '4':  ('Деление (DIV_PP_P)',                lambda: _poly_bin(DIV_PP_P, '//')),
        '5':  ('Остаток (MOD_PP_P)',                lambda: _poly_bin(MOD_PP_P, 'mod')),
        '6':  ('НОД (GCF_PP_P)',                    lambda: _poly_bin(GCF_PP_P, 'НОД')),
        '7':  ('Производная (DER_P_P)',             lambda: _poly_one(DER_P_P, "P'")),
        '8':  ('Старший коэффициент (LED_P_Q)',     lambda: _poly_lead()),
        '9':  ('Степень (DEG_P_N)',                 lambda: _poly_deg()),
        '10': ('Умножить на x^k (MUL_Pxk_P)',      lambda: _poly_mul_xk()),
        '11': ('Умножить на рац. число (MUL_PQ_P)', lambda: _poly_mul_q()),
        '12': ('Вынести множитель (FAC_P_Q)',       lambda: _poly_fac()),
        '13': ('Кратные корни → простые (NMR_P_P)', lambda: _poly_one(NMR_P_P, 'NMR')),
    }
    _run_menu("МНОГОЧЛЕНЫ", ops)


def _poly_bin(fn, op):
    print("  Введите первый многочлен:")
    a = input_polynomial("")
    print("  Введите второй многочлен:")
    b = input_polynomial("")
    try:
        r = fn(a, b)
        print(f"  ({poly_to_str(a)}) {op} ({poly_to_str(b)}) = {poly_to_str(r)}")
    except Exception as e:
        print(f"  Ошибка: {e}")


def _poly_one(fn, label):
    print("  Введите многочлен:")
    p = input_polynomial("")
    try:
        r = fn(p)
        print(f"  {label}({poly_to_str(p)}) = {poly_to_str(r)}")
    except Exception as e:
        print(f"  Ошибка: {e}")


def _poly_lead():
    print("  Введите многочлен:")
    p = input_polynomial("")
    print(f"  Старший коэффициент: {rat_to_str(LED_P_Q(p))}")


def _poly_deg():
    print("  Введите многочлен:")
    p = input_polynomial("")
    print(f"  Степень: {nat_to_str(DEG_P_N(p))}")


def _poly_mul_xk():
    print("  Введите многочлен:")
    p = input_polynomial("")
    while True:
        try:
            k = int(input("  Показатель k: "))
            if k >= 0:
                break
            print("  k должно быть >= 0.")
        except ValueError:
            pass
    r = MUL_Pxk_P(p, k)
    print(f"  ({poly_to_str(p)}) * x^{k} = {poly_to_str(r)}")


def _poly_mul_q():
    print("  Введите многочлен:")
    p = input_polynomial("")
    q = input_rational("  Рациональное число")
    r = MUL_PQ_P(p, q)
    print(f"  ({poly_to_str(p)}) * {rat_to_str(q)} = {poly_to_str(r)}")


def _poly_fac():
    print("  Введите многочлен:")
    p = input_polynomial("")
    try:
        r = FAC_P_Q(p)
        print(f"  Общий множитель: {rat_to_str(r)}")
    except Exception as e:
        print(f"  Ошибка: {e}")


# ══════════════════════════════════════════════════════════════════════════════
# Справка
# ══════════════════════════════════════════════════════════════════════════════

def show_help():
    print("""
╔══════════════════════════════════════════════════════════════╗
║              СПРАВКА — СИСТЕМА КОМПЬЮТЕРНОЙ АЛГЕБРЫ          ║
╠══════════════════════════════════════════════════════════════╣
║  Система работает с четырьмя типами математических объектов: ║
║                                                              ║
║  1. НАТУРАЛЬНЫЕ ЧИСЛА (N)                                    ║
║     Числа 0, 1, 2, 3, ...                                    ║
║     Вводятся как обычные числа: 0, 42, 1000000               ║
║                                                              ║
║  2. ЦЕЛЫЕ ЧИСЛА (Z)                                          ║
║     Числа ..., -2, -1, 0, 1, 2, ...                          ║
║     Вводятся со знаком: -42, 0, 17                           ║
║                                                              ║
║  3. РАЦИОНАЛЬНЫЕ ЧИСЛА (Q)                                   ║
║     Дроби вида числитель/знаменатель                         ║
║     Вводятся как: 3/4, -1/2, 5 (целое = 5/1)                ║
║     Дроби автоматически сокращаются                          ║
║                                                              ║
║  4. МНОГОЧЛЕНЫ (P)                                           ║
║     Вида a0 + a1*x + a2*x^2 + ...                            ║
║     Вводятся по коэффициентам: сначала степень,              ║
║     затем коэффициенты при x^0, x^1, x^2, ...               ║
║     Коэффициенты — рациональные числа                        ║
║                                                              ║
║  Все числа имеют произвольную точность (длинная арифметика)  ║
╚══════════════════════════════════════════════════════════════╝
""")


# ══════════════════════════════════════════════════════════════════════════════
# Вспомогательная функция меню
# ══════════════════════════════════════════════════════════════════════════════

def _run_menu(title, ops):
    while True:
        print(f"\n{'─'*50}")
        print(f"  {title}")
        print(f"{'─'*50}")
        for key in sorted(ops.keys(), key=lambda x: int(x)):
            print(f"  {key:>3}. {ops[key][0]}")
        print(f"    0. Назад")
        choice = input("\n  Выбор: ").strip()
        if choice == '0':
            break
        elif choice in ops:
            print()
            try:
                ops[choice][1]()
            except KeyboardInterrupt:
                print("\n  Отменено.")
        else:
            print("  Неверный выбор.")


# ══════════════════════════════════════════════════════════════════════════════
# Главное меню
# ══════════════════════════════════════════════════════════════════════════════

def main():
    print("""
╔══════════════════════════════════════════════════════════════╗
║          СИСТЕМА КОМПЬЮТЕРНОЙ АЛГЕБРЫ                        ║
║          Коллоквиум по дискретной математике                 ║
╚══════════════════════════════════════════════════════════════╝
""")
    while True:
        print("  Главное меню:")
        print("  1. Натуральные числа (N)")
        print("  2. Целые числа (Z)")
        print("  3. Рациональные числа (Q)")
        print("  4. Многочлены (P)")
        print("  5. Справка")
        print("  0. Выход")
        choice = input("\n  Выбор: ").strip()
        if choice == '1':
            menu_natural()
        elif choice == '2':
            menu_integers()
        elif choice == '3':
            menu_rationals()
        elif choice == '4':
            menu_polynomials()
        elif choice == '5':
            show_help()
        elif choice == '0':
            print("\n  До свидания!")
            sys.exit(0)
        else:
            print("  Неверный выбор.")


if __name__ == '__main__':
    main()