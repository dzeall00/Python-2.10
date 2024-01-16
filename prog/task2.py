#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Решить поставленную задачу: написать функцию,
# вычисляющую среднее гармоническое своих аргументов.
# Если функции передается пустой список аргументов,
# то она должна возвращать значение None.

def harmonic_mean(*args):
    """
    Поиск среднего гармонического аргументов
    """
    if args:
        values = [float(arg) for arg in args]
        product = 0
        for value in values:
            product += 1/value
        return round(len(values)/product, 4)
    else:
        return None


if __name__ == "__main__":
    print(harmonic_mean(4, 8, 16))
    print(harmonic_mean(3, 9, 27))
    print(harmonic_mean(2, 3, 4))
    print(harmonic_mean(31, 12, 32))
    print(harmonic_mean(5))
    print(harmonic_mean())
