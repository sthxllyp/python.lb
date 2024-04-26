#Вариант 4
def main():
    X = []
    for i in range(15):
        element = float(input("Введите число: "))
        X.append(element)
        naib = max(positiv)
        index = X.index(naib) + 1
        print("Максимальное число:", naib)
        print("Порядковый.", index)
if __name__ == "__main__":
    main()

#Вариант 6
def main():
    Z = []
    for i in range(20):
        element = float(input("Введите число: "))
        Z.append(element)
    positiv = [num for num in Z if num > 0]
    if positiv:
        naim = min(positiv)
        print("наименьший_положительный:", naim)
    else:
        print("В списке нет положительных элементов.")
if __name__ == "__main__":
    main()