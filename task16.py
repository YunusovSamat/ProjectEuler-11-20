"""
------------------------------- Задание -------------------------------
215 = 32768, сумма цифр этого числа равна 3 + 2 + 7 + 6 + 8 = 26.
Какова сумма цифр числа 21000?
"""

n = 2 ** 1000
arr = list(str(n))
for i, x in enumerate(arr):
    arr[i] = int(x)
print(__doc__)
print("Ответ:", sum(arr))
