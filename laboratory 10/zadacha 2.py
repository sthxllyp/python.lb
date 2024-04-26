#Вариант 1
str = input("Введите строку символов: ")
num = set()
for simvol in str:
    if simvol.isdigit():
        num.add(simvol)
print("Множество цифр от '0' до '9':", num)

#Вариант 9
str = input("Введите строку символов: ")
simvol = set()
for simvol in str:
    if simvol.isdigit() or simvol in "+-*/":
        simvol.add(simvol)
print("Множество цифр и знаков арифметических операций:", simvol)