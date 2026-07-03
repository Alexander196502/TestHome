from datetime import datetime, date, timedelta, time

t = tit = time(12)

# t = time(25)  # будет ошибка нельзя вводить время вне диапазона

print(t)

t = time(12, 30)

print(t)

t = time(12, 30,15)

print(t)

d = date(2020, 12, 31)  # соблюдаем порядок год, месяц, день

print(d)

# dd = date(2026, 3, 23)

dd = date.today()

print(dd)

# dt = dd + time  - нельзя разные типы данных

dt = datetime.combine(dd, t)

print(dt)

print(dd - d)

current_date = datetime.now()

print(current_date)

inp_date = input('Введите дату (дд.мм.гггг): ')

print(inp_date)

dt = datetime.strptime(inp_date, '%d.%m.%Y')

print(dt)

print((current_date - dt))

print((current_date - dt).days)

curr_date_str = current_date.strftime('%d.%m.%Y')
print(curr_date_str)
#print(datetime.strptime('12/03/1968 16:44', '%d/%m/%y %h:%m'))
print(datetime.strptime('12/03/1856 11:11', '%d/%m/%Y %H:%M'))

print(current_date.strftime('%A %d %B %Y %H:%M:%S.%f'))
print(current_date.replace(year=2033,microsecond=0))