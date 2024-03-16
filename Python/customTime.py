import datetime as dt


def weekdayNumber(weekday):
    """
    Defines what the numerical value of each day of the week is.

    @param weekday String of the day of the week
    @returns Integer equivalent of the day of the week
    """
    weekdays = {
        "Sunday" : 0,
        "Sun" : 0,
        "Monday" : 1,
        "Mon" : 1,
        "Tuesday" : 2,
        "Tues" : 2,
        "Wednesday" : 3,
        "Wed" : 3,
        "Thursday" : 4,
        "Thurs" : 4,
        "Friday" : 5,
        "Fri" : 5,
        "Saturday" : 6,
        "Sat" : 6
    }
    return weekdays[weekday]



def beginningOfWeek(date, dayWeekBegins="Sunday"):
    """
    Finds the date that begins the week of the given date, where the date that begins the week must be before the 
    specified date.

    @param date datetime specifying the date whose beginning week date is of interest
    @param String specifying what is day of the week is considered the start of the week, default value "Sunday"
    @returns datetime of the day that begins the week containing the given date
    """
    isoNum = date.isoweekday()
    weekdayNum = weekdayNumber(dayWeekBegins)
    diff = isoNum - weekdayNum
    return date - dt.timedelta(days=diff + (7 if diff < 0 else 0))



def startOfYear(date, dayYearBegins="Sunday"):
    """
    Finds the date beginning the year, defined as the first day of the week specified by dayYearBegins that is 
    occurs before or on January 1st of the given date's year.

    @param date datetime specifying the year whose start date is of interest
    @param String specifying what day of the week is considered the start of the year, default value "Sunday"
    @returns datetime of the first day of the year
    """
    return beginningOfWeek(dt.datetime(date.year, 1, 1), dayYearBegins)



def weekOfYear(date, dayYearBegins="Sunday"):
    """
    Finds the week of the year of the given date.

    @param date datetime specifying the day whose start week of the year is of interest
    @param String specifying what day of the week is considered the start of the year, default value "Sunday"
    @returns Integer of the week of the year the give date is
    """
    # Add 1 to account for the beginning for the first week
    return -(-(abs(date - startOfYear(date)).days + 1) // 7)
