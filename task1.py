# Задача 30:  Заполните массив элементами арифметической прогрессии. 
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

result = list()
def arifmet_progress (first, diff, quantity):
    for i in range(quantity):
        result.append(first + i*diff)
    return result
print(arifmet_progress(int(input('Введите первый элемент: ')), 
int(input('Введите разницу d: ')), int(input('Введите количество элементов: '))))



