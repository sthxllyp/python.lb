mnogestvo1 = set(input("Введите элементы первого множества через пробел: ").split())
mnogestvo2 = set(input("Введите элементы второго множества через пробел: ").split())
razlichn_num = mnogestvo1.symmetric_difference(mnogestvo2)
print("Различные числа в множествах:", razlichn_num )

mnogestvo1 = set(map(int, input("Введите элементы первого множества через пробел: ").split()))
mnogestvo2 = set(map(int, input("Введите элементы второго множества через пробел: ").split()))
obshie_num = sorted(mnogestvo1.intersection(mnogestvo2))
print("Числа, входящие в оба множества в порядке возрастания:", obshie_num)