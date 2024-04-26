str = input("Введите строку из слов, разделенных пробелами: ")
slv = str.split()
obratka = " ".join(slv[::-1])
print("Новая строка (слова в обратном порядке):", obratka)