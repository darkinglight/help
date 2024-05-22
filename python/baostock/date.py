import datetime


def today():
    day = datetime.date.today()
    weekday = day.weekday()
    if weekday > 4:
        day = day - datetime.timedelta(days=weekday-4)
    return day.strftime("%Y-%m-%d")


if __name__ == "__main__":
    print(today())
