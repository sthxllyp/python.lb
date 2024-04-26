stroka = input("Введите строку: ")
clear = stroka.replace(" ", "")
if clear == clear[::-1]:
    print("Это палиндром")
else:
    print("Это не палиндром")