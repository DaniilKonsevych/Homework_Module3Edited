from datetime import datetime

def get_days_from_today(date):

    try:
        date_object = datetime.strptime(date, '%Y-%m-%d')
    except:
        date_object = datetime(year = 1, month =  1, day = 1)
        print("When calling the function, invalid data was inputed. Setting date to default. (Tip: the format of the inputed data should be: YYYY-MM-DD)")

    current_date = datetime.today()

    days_after_specific_date = current_date.toordinal() - date_object.toordinal()
    
    return days_after_specific_date

print(f"Days since the set date: {get_days_from_today('2050-07-03')}")
print(f"Days since the set date: {get_days_from_today('2050 07 03')}")