import random
import math
colvo = 0
while colvo < 10:
    num = random.randint(-10, 10)
    if num < 0:
        continue
    elif num == 0:
        break
    sqrt = math.sqrt(num)
    print(f"Квадратный корень числа {num}:", sqrt)
    colvo += 1