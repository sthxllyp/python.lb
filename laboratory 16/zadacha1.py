import math
def calculate_expression(x, y, z):
    first_term = math.sqrt(x**2 + z**2 + math.cos(x * z)**3)
    second_term = math.sqrt(y**2 + x**2 + math.cos(y * x)**3)
    third_term = math.sqrt(z**2 + y**2 + math.cos(z * y)**3)
    result = (first_term + second_term) / third_term
    return result
x = float(input("Введите значение x: "))
y = float(input("Введите значение y: "))
z = float(input("Введите значение z: "))
result = calculate_expression(x, y, z)
print("Значение выражения L =", result)