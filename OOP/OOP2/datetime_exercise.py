import datetime as dt


def days_until_birthday(birthday):
    """How long until my next birthday?"""
    today_date = dt.datetime.today()

    if birthday.month > today_date.month or (birthday.month == today_date.month and birthday.day > today_date.day):
        next_birthday = dt.datetime(today_date.year, birthday.month, birthday.day)
    else:
        next_birthday = dt.datetime(today_date.year + 1, birthday.month, birthday.day)

    return (next_birthday - today_date).days

def double_day(b1, b2):
    """Compute the day when one person is twice as old as the other.

    b1: datetime birthday of the younger person
    b2: datetime birthday of the older person
    """

    def get_age(birthday, current_date):
        return current_date.year - birthday.year - ((current_date.month, current_date.day) < (birthday.month, birthday.day))

    day_compare = b1

    while get_age(b1, day_compare) * 2 != get_age(b2, day_compare):
        day_compare += dt.timedelta(days=1)
    
    return day_compare


def datetime_exercises():
    """Exercise solutions."""

    # print today's day of the week
    print(dt.datetime.today().weekday())

    # compute the number of days until the next birthday
    # (note that it usually gets rounded down)
    birthday = dt.datetime(1997, 10, 25)
    print('Days until birthday', end=' ')
    print(days_until_birthday(birthday))

    # compute the day one person is twice as old as another
    b1 = dt.datetime(2017, 12, 25)
    b2 = dt.datetime(2010, 11, 1)
    print('Double Day', end=' ')
    print(double_day(b1, b2))


# def main():
#     datetime_exercises()


if __name__ == '__main__':
    datetime_exercises()
