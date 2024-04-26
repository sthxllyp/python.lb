import random
B = int(input("Введите размерность квадратной матрицы: "))
mat = [[random.randint(-10,10) for x in range(B)]for y in range(B)]
print("Исходная матрица:")
for r in mat: 
    print(*r)
otr_sum = 0
for i in range(B):
    for j in range(B-i, B):
        if mat[i][j] < 0:
            otr_sum += mat[i][j]
print("Сумма отрицательных элементов под дополнительной диагональю",otr_sum)