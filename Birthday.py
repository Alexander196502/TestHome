from datetime import datetime, date, timedelta, time, UTC
birthdate = input('ВВедите дату рождения (дд.мм.гггг): ')
birthdate = datetime.strptime(birthdate, '%d.%m.%Y')  # из str в datetime
birthdate = birthdate.date()  # из datetime в date
current_date = date.today()
yyear = current_date.year
birthday = birthdate.replace(year=yyear)  # Замена в дате рождения года на текущий