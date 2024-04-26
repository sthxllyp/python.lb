import random
count = 0
A = [random.randint(-10,10) for x in range(20)]
print("Сгенерированный список: ",A)
count = sum(1 for x in A if x < 0)
print("Количество отрицательных чисел: ",count)