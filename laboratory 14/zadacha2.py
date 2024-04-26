#Вариант 1
def find_students(students, specialty):
    found_students = [student[0] for student in students if student[1] == specialty]
    if found_students:
        return ", ".join(found_students)
    else:
        return "Проверьте запрос"
def main():
    n = int(input("Введите количество студентов: "))
    student_dict = {}
    for _ in range(n):
        student_info = input("Введите информацию о студенте (фамилия специальность группа): ").split()
        surname, specialty, group = student_info
        if specialty not in student_dict:
            student_dict[specialty] = []
        student_dict[specialty].append(surname)
    query = input("Введите название специальности для поиска: ")
    result = find_students(student_dict.get(query, []), query)
    print("Найденные студенты:", result)
if __name__ == "__main__":
    main()

#Вариант 2
    def find_specialty(specialties, group_number):
        for specialty, groups in specialties.items():
            return specialty
    return ""
def main():
    n = int(input("Введите количество специальностей: "))
    specialty_dict = {}
    for _ in range(n):
        specialty_info = input("Введите информацию о специальности (название-номера групп через запятую): ").split('-')
        specialty, groups = specialty_info[0], specialty_info[1].split(',')
        for group in groups:
            if group not in specialty_dict:
                specialty_dict[group] = specialty
    query = input("Введите номер группы для поиска: ")
    result = find_specialty(specialty_dict, query)
    print("Название специальности:", result)
if __name__ == "__main__":
    main()

#Вариант 3
    def create_dictionary(word):
        letter_count = {}
    for letter in word:
        if letter in letter_count:
            letter_count[letter] += 1
        else:
            letter_count[letter] = 1
    return letter_count
def main():
    word = input("Введите слово: ")
    result_dict = create_dictionary(word)
    print("Словарь:", result_dict)
if __name__ == "__main__":
    main()