#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# Сумма модулей аргументов, расположенных после первого аргумента, равного нулю


def summa(*args):
    if args:
        return sum(map(abs, args[args.index(0) + 1:]))

    else:
        return None


if __name__ == '__main__':
    print(f'Сумма = {summa(7, -3, 8, 0, -1, 5, 1)}')
    print(f'Сумма = {summa()}')