import csv
import datetime


# функция, которая генерирует даты начиная с указанной даты
def generate_dates(start_date, num_months):
    dates = []
    for i in range(num_months):
        year = start_date.year
        month = start_date.month + i
        if month > 12:
            year += 1
            month -= 12
        date = start_date.replace(year=year, month=month)
        dates.append(date)
    return dates


# задаем начальную дату и количество месяцев
start_date = datetime.date(2020, 1, 1)
num_months = 12

# создаем список дат
dates = generate_dates(start_date, num_months)

# создаем список расходов, заданный вручную
electricity_usage = [30, 20, 25, 28, 32, 35, 40, 45, 50, 55, 60, 65]

# создаем CSV-файл
with open('dataset.csv', 'w', newline='') as file:
    writer = csv.writer(file, delimiter=';')
    writer.writerow(['Date', 'Electricity Usage'])
    for i in range(num_months):
        writer.writerow([dates[i].strftime('%d.%m.%Y'), electricity_usage[i]])
