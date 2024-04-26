nab_chis = list(map(int, input("Введите набор целых чисел, разделенных пробелами: ").split()))
begin, ending = map(int, input("Введите два целых числа, начало и конец интервала для суммирования: ").split())
sum_kv = sum(x**2 for x in nab_chis[begin:ending+1])
print(f"Сумма квадратов чисел от {begin} до {ending}: {sum_kv}")