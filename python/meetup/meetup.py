import datetime
from calendar import monthrange, day_name


def meetup_day(year, month, name, desc):
    day = next(number for number, day_n in enumerate(day_name, start=1)
               if day_n == name)
    description = {
        'teenth':   13,
        '1st':      1,
        '2nd':      8,
        '3rd':      15,
        '4th':      22,
        '5th':      29,
        'last':     monthrange(year, month)[1] - 6
    }
    start_day = description[desc]

    while datetime.date(year, month, start_day).isoweekday() != day:
        start_day += 1

    return datetime.date(year, month, start_day)
