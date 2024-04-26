import math
def S(r):
    """Функция для вычисления площади круга."""
    return math.pi * r**2
def l(r):
    """Функция для вычисления длины окружности."""
    return 2 * math.pi * r
def krug():
    """Функция для взаимодействия с пользователем и вывода результатов."""
    radius = float(input("Введите радиус окружности: "))
    area = S(radius)
    circumference = l(radius)
    print("Площадь круга:", area)
    print("Длина окружности:", circumference)
krug()