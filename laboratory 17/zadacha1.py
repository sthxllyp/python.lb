import random
import string
def generate_password(length):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))
def generate_unique_passwords(N, length):
    passwords = set()
    while len(passwords) < N:
        passwords.add(generate_password(length))
    return passwords
N = int(input("Введите количество паролей: "))
K = int(input("Введите длину паролей: "))
passwords = generate_unique_passwords(N, K)
print("Сгенерированные пароли:")
for password in passwords:
    print(password)