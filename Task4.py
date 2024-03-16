from datetime import datetime, timedelta

users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"},
    {"name": "Jonathan Brando", "birthday" : "1992.03.18"},
    {"name": "Antonio Brando", "birthday" : "1992.03.23"}
]

def get_up_coming_birthdays(users):
    
    def find_next_weekday(d, weekday : int):
        days_ahead = weekday - d.weekday()
        if days_ahead <= 0:
            days_ahead += 7
        return d + timedelta(days=days_ahead)

    def date_convert(users):
        prepared_users = []
        for user in users:
            try:
                birthday = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
                prepared_users.append({"name": user["name"], "birthday" : birthday})
            except ValueError:
                print(f"Invalid birthday date format for user {user}")
        return prepared_users

    def congratulation(prepared_users):
        days = 7
        today = datetime.today().date()
        upcoming_birthdays = []
        for user in prepared_users:
            birthday_this_year = user["birthday"].replace(year=today.year)

            if 0 <= (birthday_this_year - today).days <= days:
                if birthday_this_year.weekday() >= 5:
                    birthday_this_year = find_next_weekday(birthday_this_year, 0)
        
            congratulation_date_str = birthday_this_year.strftime("%Y.%m.%d")
            
            if birthday_this_year > today and birthday_this_year < birthday_this_year + timedelta(days=7):
                upcoming_birthdays.append({
                    "name": user["name"],
                    "congratulation_date" : congratulation_date_str
                })
        return upcoming_birthdays
    return congratulation(date_convert(users))

print(get_up_coming_birthdays(users))