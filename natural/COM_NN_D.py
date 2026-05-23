def COM_NN_D(a, b):
    # Число с большим количеством цифр заведомо больше
    if a['n'] != b['n']:
        return 2 if a['n'] > b['n'] else 1
 
    # Одинаковое кол-во цифр — сравниваем поразрядно от старшей к младшей
    for i in range(a['n'], -1, -1):
        if a['digits'][i] != b['digits'][i]:
            return 2 if a['digits'][i] > b['digits'][i] else 1
 
    return 0  # все цифры совпали — числа равны