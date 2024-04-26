import random
def generate_schedule(num_exams, subjects):
    days = ['понедельник', 'вторник', 'среда', 'четверг', 'пятница']
    times = [9 + 0.5 * i for i in range(10)] 
    tickets = list(range(1, 21)) 
    for subject in subjects:
        day = random.choice(days)
        time = random.choice(times)
        ticket = random.choice(tickets)
        print(f"Экзамен по дисциплине «{subject}» состоится в {day}, время {int(time)}:30. Ваш счастливый билет N {ticket}.")
        tickets.remove(ticket)
num_exams = int(input("Введите количество экзаменов: "))
subjects = input("Введите наименование дисциплин через запятую и пробел: ").split(", ")
generate_schedule(num_exams, subjects)