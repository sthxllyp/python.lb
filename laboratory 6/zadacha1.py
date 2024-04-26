import math
k = int(input("Введите число k:"))
for num in range(k + 1):
    sqrt = math.sqrt(num)
cub = num ** 3
print(f"Корень числа {num} равен {sqrt}, а куб равен {cub}")