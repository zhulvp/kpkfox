x = int(input())
"""Пишем алгоритм. в котором вводится длинное число, 
которое в программе разбивается на отдельные числа
"""
while x:
    digit = x%10
    print(digit, x)
    x //=10 # Выделяем отдельно каждую цифру
    """
    Алгоритм работает только 
    для положительных чисел"""

