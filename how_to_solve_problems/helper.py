
days_of_months = [31 ,28 ,31 ,30 ,31 ,30 ,31 ,31 ,30 ,31 ,30 ,31]
days_of_months_with_leap_year = [31 ,29 ,31 ,30 ,31 ,30 ,31 ,31 ,30 ,31 ,30 ,31]

def is_leap_year(year):
    if(year % 400 == 0):
        return True
    elif(year % 100 == 0):
        return False
    elif(year % 4 == 0):
        return True
    else:
        return False

def nextDayDate(year,month,day):
    if(is_leap_year(year)):
        days_of_month = days_of_months_with_leap_year[month - 1]
    else:
        days_of_month = days_of_months[month - 1]
    if(day == days_of_month):
        day = 1
        if(month == 12):
            month = 1
            year += 1
        else:
            month += 1
    else:
        day += 1

    return year,month,day

def checkIfDateIsBigger(year1,month1,day1,year2,month2,day2):
    if(year1 < year2):
        return True
    elif(year1 == year2):
        if(month1 < month2):
            return True
        elif(month1 == month2):
            if(day1 < day2):
                return True
    return False

def checkInvalidDay(year,month,day):
    if(is_leap_year(year)):
        if(not(day <= days_of_months_with_leap_year[month - 1])):
            return True
    else:
        if (not (day <= days_of_months[month - 1])):
            return True

def checkIfValidDates(year1,month1,day1,year2,month2,day2):
    per_date_validity =  True
    if(month1 > 12 or month2 > 12):
        per_date_validity =  False
    else:
        if(checkInvalidDay(year1,month1,day1)):
            per_date_validity =  False
        if(checkInvalidDay(year2,month2,day2)):
            per_date_validity =  False
    if(per_date_validity):
        return checkIfDateIsBigger(year1,month1,day1,year2,month2,day2)
    else:
        return False


def daysBetweenDates(year1, month1, day1, year2, month2, day2):
    """
    Calculates the number of days between two dates.
    """
    days = 0
    assert checkIfValidDates(year1,month1,day1,year2,month2,day2)
    while(checkIfDateIsBigger(year1,month1,day1,year2,month2,day2)):
        days += 1
        year1,month1,day1 = nextDayDate(year1,month1,day1)
    return days


