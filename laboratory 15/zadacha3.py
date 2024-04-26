def process_lists(list1, a, b, c):
    """Функция для обработки двух списков."""
    filtered_elements = [num for num in list1 if num > a and num < b and num % c == 0]
    sum_of_others = sum([num for num in list1 if num not in filtered_elements])
    print("Элементы, которые соответствуют условиям:", filtered_elements)
    print("Сумма остальных элементов списка:", sum_of_others)
list1 = [1, 4, 7, 10, 13, 16, 19]
a = 5
b = 20
c = 3
process_lists(list1, a, b, c)