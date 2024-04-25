#вариант 5
a = float(input("Введите значение a: "))
b = float(input("Введите значение b: "))
c = float(input("Введите значение c: "))
calculator = 0
if a < 0:
    calculator +=1
if b < 0:
    calculator +=1
if c < 0:
    calculator +=1
print("Количество отрицательных чисел среди a, b и c:",calculator,)   

#вариант 6
a = float(input("Введите значение a: "))
b = float(input("Введите значение b: "))
c = float(input("Введите значение c: "))
calculator = 0
if a > 0:
    calculator +=1
if b > 0:
    calculator +=1
if c > 0:
    calculator +=1
print("Количество положительных чисел среди a, b и c:",calculator,)  

#вариант 9
m = float(input("Введите массу первого пакета(в кг): "))
n = float(input("Введите массу второго пакета(в кг): "))
if m > n:
    print("Первый пакет тяжелее второго.")
elif m < n:
    print("Второй пакет тяжелее первого.")
else:
    print("Масса пакетов одинакова.")
    






