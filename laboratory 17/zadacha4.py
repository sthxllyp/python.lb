from datetime import datetime, timedelta
import calendar
def is_lucky_date(date):
    day = date.day
    weekday = calendar.day_name[date.weekday()]
    if day % 4 != 0 and weekday != 'Monday':
        return True
    else:
        return False
def find_lucky_dates(start_date, n, count):
    lucky_dates = []
    current_date = start_date
    while len(lucky_dates) < count:
        if is_lucky_date(current_date):
            lucky_dates.append(current_date)
        current_date += timedelta(days=n)
    return lucky_dates
start_date_str = input("Введите исходную дату в формате YYYY/MM/DD: ")
start_date = datetime.strptime(start_date_str, "%Y/%m/%d")
n = int(input("Введите число n: "))
lucky_dates = find_lucky_dates(start_date, n, 3)
print("Счастливые даты:")
for date in lucky_dates:
    formatted_date = date.strftime("%d %B, %A")
    print(formatted_date)