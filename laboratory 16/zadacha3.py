#Вариант 1
def is_divisible_by_eight_and_three_digit(num):
    """Функция для проверки, является ли число трехзначным и делится ли на 8."""
    return num % 8 == 0 and 100 <= num <= 999
def cube(num):
    """Функция для возведения числа в куб."""
    return num ** 3
def main():
    """Основная функция программы."""
    numbers_str = input("Введите числа через пробел: ")
    numbers_list = list(map(int, numbers_str.split()))
    filtered_numbers = filter(is_divisible_by_eight_and_three_digit, numbers_list)
    cubed_numbers = map(cube, filtered_numbers)
    sum_of_cubed_numbers = sum(cubed_numbers)
    print("Сумма кубов всех трехзначных чисел, делящихся на 8:", sum_of_cubed_numbers)
main()

#Вариант 3
def print_even_numbers(numbers):
    """Функция для печати четных чисел из списка."""
    even_numbers = filter(lambda x: x % 2 == 0, numbers)
    print("Четные числа из списка:", list(even_numbers))
def main():
    """Основная функция программы."""
    numbers_str = input("Введите числа через пробел: ")
    numbers_list = list(map(int, numbers_str.split()))
    print_even_numbers(numbers_list)
main()

#Вариант 8
def print_odd_numbers(numbers):
    """Функция для печати нечетных чисел из списка."""
    odd_numbers = filter(lambda x: x % 2 != 0, numbers)
    print("Нечетные числа из списка:", list(odd_numbers))
def main():
    """Основная функция программы."""
    numbers_str = input("Введите числа через пробел: ")
    numbers_list = list(map(int, numbers_str.split()))
    print_odd_numbers(numbers_list)
main()

