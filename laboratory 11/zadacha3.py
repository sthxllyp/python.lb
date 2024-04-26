#Вариант 5
def main():
    num = []
    for i in range(10):
        num = float(input("Введите вещественное число: "))
        num.append(num)
    num.sort(reverse=True)
    print("отсортированный список:", num)
if __name__ == "__main__":
    main()

#Вариант 9
    def main():
        spisok = []
    for i in range(14):
        num = int(input("Введите целое число: "))
        spisok.append(num)
    spisok.reverse()
    print("переставленный список:", spisok)
if __name__ == "__main__":
    main()