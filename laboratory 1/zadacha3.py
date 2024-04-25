def sum(l, n, v):   
     return l + n + v
l = int(input("Введите первое число:"))
n = int(input("Введите второе число:"))
v = int(input("Введите третье число:"))
print("Сумма чисел = ", sum(l,n,v))

def umnozh(l, n, v):
    return l * n * v
l = int(input("Введите первое число:"))
n = int(input("Введите второе число:"))
v = int(input("Введите третье число:"))
print("Произведение чисел = ", umnozh(l,n,v))

def srarifm(l, n, v):
    return (l + n + v)/3
l = int(input("Введите первое число:"))
n = int(input("Введите второе число:"))
v = int(input("Введите третье число:"))
print("Среднее арифметическое чисел = ", srarifm(l,n,v))