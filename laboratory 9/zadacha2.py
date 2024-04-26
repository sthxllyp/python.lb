#Вариант 3
str = input("Введите строку: ")
result = ""
for simvol in str:
    result += simvol * 2
print("Результат:", result)

#Вариант 8
name = input("Введите имя файла: ")
part_name = name.split(".")
extension = part_name[-1]
print("Расширение файла:", extension)