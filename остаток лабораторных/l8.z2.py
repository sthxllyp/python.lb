stroka = "Ваша строка; с точкой с запятой"
poz = stroka.find(';')
if poz != -1:
    count = poz
    print(f"Количество символов до точки с запятой: {count}")
else:
    print("Точка с запятой не найдена в строке.")