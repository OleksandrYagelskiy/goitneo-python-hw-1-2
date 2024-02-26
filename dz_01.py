import datetime
from collections import defaultdict

def get_birthdays_per_week(users):
    today = datetime.datetime.today().date()
    birthdays = defaultdict(list)

    for user in users:
        name = user["name"]
        birthday = user["birthday"].date()  # Конвертуємо дату народження до типу date

        birthday_this_year = birthday.replace(year=today.year) # Визначаємо день народження на цьому році

        if birthday_this_year < today: # Якщо день народження вже минув, то визначаємо день народження на наступному році
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)

        delta_days = (birthday_this_year - today).days # Визначаємо різницю між днем народження та поточною датою

        day_of_week = (today + datetime.timedelta(days=delta_days)).strftime('%A') # Визначаємо день тижня для дня народження

        if day_of_week in ['Saturday', 'Sunday']: # Якщо день народження вихідний, переносимо його на понеділок

            day_of_week = 'Monday'

        birthdays[day_of_week].append(name) # Зберігаємо ім'я користувача в відповідний день тижня

    for day, users in birthdays.items(): # Виводимо імена іменинників по днях тижня у відповідному форматі
        print(f"{day}: {', '.join(users)}")

users = [
    {"name": "Andrey Gorobets", "birthday": datetime.datetime(1985, 11, 28)},
    {"name": "Oleh Kavun", "birthday": datetime.datetime(1996, 2, 22)},
    {"name": "Dmutro Dzun", "birthday": datetime.datetime(1990, 11, 16)},
    {"name": "Juliya Valenneus", "birthday": datetime.datetime(1994, 9, 21)}
] # Приклад використання:

get_birthdays_per_week(users)
