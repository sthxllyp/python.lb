def find_phone(numbers, name):
    for number, owner in numbers:
        if owner == name:
            return number
    return "Нет в телефонной книге"
def main():
    n = int(input())
    phone_book = [input().split() for _ in range(n)]
    query = input()
    result = find_phone(phone_book, query)
    print(result)
if __name__ == "__main__":
    main()