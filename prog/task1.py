#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Решить поставленную задачу: написать функцию,
# вычисляющую среднее геометрическое своих аргументов
# Если функции передается пустой список аргументов,
# то она должна возвращать значение None.

def geometric_mean(*args):
    """
    Поиск среднего геометрического аргументов
    """
    if args:
        values = [float(arg) for arg in args]
        product = 1.0
        for value in values:
            product *= value
        return round(pow(product, 1/len(values)), 4)
    else:
        return None


if __name__ == "__main__":
    print(geometric_mean(4, 8, 16))
    print(geometric_mean(3, 9, 27))
    print(geometric_mean(2, 3, 4))
    print(geometric_mean(31, 12, 32))
