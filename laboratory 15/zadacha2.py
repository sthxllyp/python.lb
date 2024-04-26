#Вариант 1
def filter_even_above_10(numbers):
    """Функция для фильтрации четных чисел больше 10."""
    filtered_numbers = [num for num in numbers if num > 10 and num % 2 == 0]
    return filtered_numbers
def main():
    """Основная функция программы."""
    numbers_str = input("Введите числа через пробел: ")
    numbers_list = list(map(int, numbers_str.split()))
    filtered_list = filter_even_above_10(numbers_list)
    print("Исходный список:", numbers_list)
    print("Отфильтрованный список (четные числа больше 10):", filtered_list)
main()

#Вариант 2
def count_spaces_and_check_even(string):
    """Функция для подсчета пробелов в строке и проверки на четность их количества."""
    space_count = string.count(' ')
    if space_count % 2 == 0:
        print("Четное число")
    else:
        print("Нечетное число")
def main():
    """Основная функция программы."""
    input_string = input("Введите строку: ")
    count_spaces_and_check_even(input_string)
main()

#Вариант 3
def print_average_of_list(numbers):
    """Функция для печати среднего значения элементов списка."""
    if not numbers:
        print("Список пустой. Среднее значение: 0")
    else:
        average = sum(numbers) / len(numbers)
        print("Среднее значение элементов списка:", average)
def main():
    """Основная функция программы."""
    numbers_str = input("Введите числа через пробел: ")
    numbers_list = list(map(int, numbers_str.split()))
    print_average_of_list(numbers_list)
main()