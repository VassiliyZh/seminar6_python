# Задача 32: Определить индексы элементов массива (списка), значения 
# которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)
from random import randint
indexes = list()
def indexes_array (min_number, max_number, array):
    for index, number in enumerate(array):
        if min_number<=number<=max_number:
            indexes.append(index)
    return indexes
array = [randint(-10,10) for i in range(10)]
print(array)
print(indexes_array(int(input('Введите минимальное число: ')), 
int(input('Введите максимальное число: ')), array))

