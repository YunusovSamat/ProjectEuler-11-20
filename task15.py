"""
------------------------------- Задание -------------------------------
Начиная в левом верхнем углу сетки 2×2 и имея возможность двигаться
только вниз или вправо, существует ровно 6 маршрутов
до правого нижнего угла сетки.
Сколько существует таких маршрутов в сетке 20×20?
"""


def sum_point(t_i, t_j, t_arr):
    return arr[t_i][t_j+1] + arr[t_i+1][t_j]


n = 20 + 1
m = 20 + 1
arr = [[0 for j in range(n)] for i in range(m)]

for i in range(m):
    arr[i][n-1] = 1
for j in range(n):
    arr[m-1][j] = 1

a = m - 2
b = n - 2
while (a >= 0) and (b >= 0):
    for i in range(a, -1, -1):
        arr[i][b] = sum_point(i, b, arr)
    if b >= 0:
        b -= 1
    for j in range(b, -1, -1):
        arr[a][j] = sum_point(a, j, arr)
    if a >= 0:
        a -= 1

print(__doc__)
print("Ответ:", arr[0][0])
