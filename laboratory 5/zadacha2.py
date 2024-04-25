#вариант 4
k = 3
sum = 0
num = 1000
while num <= 9999:
    if num % k == 0:
        sum += num
    num += 1
print("Сумма всех 4-значных чисел, кратных", k, ":", sum)

#вариант 5
n = 25
sum = 0
proizv = 1
count = 0
while count < n:
    number = float(input(f"Введите число {count + 1}: "))
    sum += number
    proizv *= number
    count += 1
print("Сумма введенных чисел:", sum)
print("Произведение введенных чисел:", proizv)