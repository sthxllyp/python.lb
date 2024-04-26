#Вариант 2
import random 
M = int(input("Введите количество строк в матрице: ")) 
N = int(input("Введите количество столбцов в матрице: ")) 
matrica = [[random.randint(1,50) for x in range(N)] for y in range(M)] 
print("Исходная матрица:") 
for r in matrica:  
    print(*r) 
print("Сумма элементов  каждой строки:") 
for r in matrica: 
    r_sum = sum(r)     
    print(r_sum)

#Вариант 4
import random 
A = int(input("Введите размерность квадратной матрицы: ")) 
mat = [[random.randint(-10,10) for x in range(A)]for y in range(A)] 
print("Исходная матрица:") 
for r in mat:  print(*r) 
negativ = 0 
for i in range(A): 
    for j in range(i): 
        if mat[i][j] < 0: 
            negativ += mat[i][j] 
            print("Сумма отрицательных элементов над главной диагональю",negativ)