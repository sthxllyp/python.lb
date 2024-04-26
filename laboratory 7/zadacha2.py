#Вариант 1
for i in range(1, 6):
    for j in range(i):
        print(i, end=" ") 
    print()


#Вариант 5
N = 3  
M = 6  
for i in range(N):
    for j in range(M):
        if (i % 2 == 0 and j % 2 == 0) or (i % 2 != 0 and j % 2 != 0):
            print("+", end=" ")
        else:
            print("-", end=" ")
    print() 