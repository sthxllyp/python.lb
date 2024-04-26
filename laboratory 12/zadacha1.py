import random 
M = int(input("Введите количество строк в матрице: ")) 
matrix = [[random.randint(1,20) for x in range(4)] for y in range(M)] 
print("Исходная матрица:") 
for row in matrix:     
    print(*row) 
for i in range(len(matrix)):      
    if i % 2 == 0:  
        print('\n',*matrix[i])     
    else:  
        print('\n',*matrix[i][::-1])