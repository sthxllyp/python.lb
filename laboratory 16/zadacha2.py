def factorial(num):
    if num == 0:
        return 1
    else:
         return num * factorial(num - 1)
def calculate_expression(n, m):
     C = factorial(n) // (factorial(m) * factorial(n - m))
     return C
n = int(input("Введите значение n: "))
m = int(input("Введите значение m: "))
result = calculate_expression(n, m)
print("Значение выражения C =", result)