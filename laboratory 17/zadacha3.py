from datetime import datetime, timedelta
def exam_date(days_until_exam):
    current_date = datetime.now()
    exam_date = current_date + timedelta(days=days_until_exam)
    formatted_date = exam_date.strftime("%d %B") 
    return formatted_date
days_until_exam = int(input("Введите количество дней до экзамена: "))
exam_date = exam_date(days_until_exam)
print("Дата экзамена:", exam_date)