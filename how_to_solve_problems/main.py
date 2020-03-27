from helper import daysBetweenDates

def testDaysBetweenDates():
    #     test same day
    assert (daysBetweenDates(2017, 12, 30,
                             2017, 12, 30) == 0)
    # test adjacent days
    assert (daysBetweenDates(2017, 12, 30,
                             2017, 12, 31) == 1)
    # test new year
    assert (daysBetweenDates(2017, 12, 30,
                             2018, 1, 1) == 2)
    # test full year difference
    assert (daysBetweenDates(2012, 6, 29,
                             2013, 6, 29) == 365)

    print(daysBetweenDates(2013, 1, 1, 1999, 12, 31))
    print(daysBetweenDates(1991, 3, 1, 1991, 1, 3))

    print("Congratulations! Your daysBetweenDates")
    print("function is working correctly!")


if __name__ == "__main__":
    testDaysBetweenDates()

