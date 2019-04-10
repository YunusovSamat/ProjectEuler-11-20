"""
------------------------------- Задание -------------------------------
Последовательность треугольных чисел образуется путем сложения
натуральных чисел. К примеру, 7-ое треугольное число равно
1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. Первые десять треугольных чисел:
1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
Перечислим делители первых семи треугольных чисел:

     1: 1
     3: 1, 3
     6: 1, 2, 3, 6
    10: 1, 2, 5, 10
    15: 1, 3, 5, 15
    21: 1, 3, 7, 21
    28: 1, 2, 4, 7, 14, 28

Как мы видим, 28 - первое треугольное число, у которого более пяти
делителей.
Каково первое треугольное число, у которого более пятисот делителей?
"""

from ProjectEuler.Task1_10 import task10


def search_all_dividers(n):

    def enumeration_dividers(arr, a=1):
        a *= arr[0]
        div_set.add(a)
        div_set.add(n // a)
        for i in range(1, len(arr)):
            enumeration_dividers(arr[i:], a)

    prime_arr = []
    temp_n = n
    for b in prime_all:
        while temp_n % b == 0:
            prime_arr.append(b)
            temp_n = temp_n // b
        if temp_n == 1:
            break
    div_set = set()
    enumeration_dividers(prime_arr)
    return div_set


prime_all = task10.eratosthen(100000)
prime_all.insert(0, 2)

x = 3
y = 3
m = 2
while m < 500:
    x += y
    y += 1
    m = len(search_all_dividers(x))
print(__doc__)
print("Ответ:", x)

