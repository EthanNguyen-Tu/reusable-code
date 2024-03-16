import unittest
import datetime as dt
import customTime as ct

class CustomTimeTests(unittest.TestCase):

    def setUp(self):
        """
        days - specifies the days of the week and its abbreviations
        @returns None
        """
        self.days = ["Sunday", "Sun", "Monday", "Mon", "Tuesday", "Tues", "Wednesday", "Wed", 
                     "Thursday", "Thurs", "Friday", "Fri", "Saturday", "Sat"]


    def test_weekdayNumbers(self):
        """
        Checks for correct weekday number mapping where Sunday = 0, Monday = 1, ... Saturday = 6.
        @returns None
        """
        for i in range(len(self.days)):
            actual = ct.weekdayNumber(self.days[i])
            expected = i//2
            self.assertEqual(actual, expected, msg="Incorrect mapping for " + self.days[i] 
                             + ". Expected " + str(expected) + " but got " + str(actual) + ".")
        print('\nPassed test_weekdayNumbers')
    

    def test_beginningOfWeek(self):
        testDate = dt.datetime(1965, 2, 8)
        expected = [dt.datetime(1965, 2, 7), dt.datetime(1965, 2, 8), dt.datetime(1965, 2, 2), dt.datetime(1965, 2, 3),
                    dt.datetime(1965, 2, 4), dt.datetime(1965, 2, 5), dt.datetime(1965, 2, 6)]
        for i in range(len(self.days)):
            actual = ct.beginningOfWeek(testDate, self.days[i])
            self.assertEqual(actual, expected[i//2], msg="Incorrect day for " + self.days[i] 
                             + ". Expected " + str(expected[i//2]) + " but got " + str(actual) + ".")
        print('\nPassed test_beginningOfWeek')


    def test_startOfYear(self):
        testDate = dt.datetime(1965, 2, 8)
        expected = [dt.datetime(1964, 12, 27), dt.datetime(1964, 12, 28), dt.datetime(1964, 12, 29), dt.datetime(1964, 12, 30),
                    dt.datetime(1964, 12, 31), dt.datetime(1965, 1, 1), dt.datetime(1964, 12, 26)]
        for i in range(len(self.days)):
            actual = ct.startOfYear(testDate, self.days[i])
            self.assertEqual(actual, expected[i//2], msg="Incorrect day for " + self.days[i] 
                             + ". Expected " + str(expected[i//2]) + " but got " + str(actual) + ".")
        print('\nPassed test_startOfYear')


    def test_weekOfYear(self):
        testDates = [dt.datetime(1965, 2, 8), dt.datetime(1965, 3, 8), dt.datetime(1965, 4, 8),
                     dt.datetime(1965, 2, 14), dt.datetime(1965, 3, 14), dt.datetime(1965, 4, 14)]
        expected = [7, 11, 15, 8, 12, 16]
        for i in range(len(testDates)):
            actual = ct.weekOfYear(testDates[i])
            self.assertEqual(actual, expected[i], msg="Incorrect week number for " + str(testDates[i]) 
                             + ". Expected " + str(expected[i]) + " but got " + str(actual) + ".")
        print('\nPassed test_weekOfYear')


if __name__ == '__main__':
    unittest.main()
