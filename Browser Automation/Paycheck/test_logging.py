import unittest
import logging

class TestLogging(unittest.TestCase):
    def setUp(self):
        log = open("test.txt", "r")
        self.oldData = log.readlines()
        log.close()

    def tearDown(self):
        log = open("test.txt", "w")
        log.writelines(self.oldData)
        log.close()

    def test_Hours(self):
        hourlyPay = 15

        logging.clock_hours("3/5/2022", "6", hourlyPay, "test.txt")

        log = open("test.txt", "r")
        data = log.readlines()
        updatedPay = int(data[0])
        newestLog = data[-1]
        log.close()

        self.assertEqual(updatedPay, 144)
        self.assertEqual(newestLog, "3/5/2022: 6 hours worked\n")

        logging.clock_hours("3/6/2022", "10", hourlyPay, "test.txt")
        logging.clock_hours("3/7/2022", "2", hourlyPay, "test.txt")
        logging.clock_hours("3/10/2022", "4", hourlyPay, "test.txt")

        log = open("test.txt", "r")
        data = log.readlines()
        updatedPay = int(data[0])
        logOne = data[-3]
        logTwo = data[-2]
        logThree = data[-1]
        log.close()

        self.assertEqual(updatedPay, 384)
        self.assertEqual(logOne, "3/6/2022: 10 hours worked\n")
        self.assertEqual(logTwo, "3/7/2022: 2 hours worked\n")
        self.assertEqual(logThree, "3/10/2022: 4 hours worked\n")

    def test_Pay(self):
        logging.add_pay("34", "test.txt")
        
        log = open("test.txt", "r")
        data = log.readlines()
        log.close()

        newOwed = data[0]
        self.assertEqual(newOwed, "20\n")
        
        i = 1
        for logInstance in data[1:-1]:
            self.assertEqual(logInstance, self.oldData[i])
            i += 1

        lastLog = data[-1]
        self.assertEqual(lastLog, "$34 paid. Old total: 54. New total: 20\n")
        

if __name__ == '__main__':
    unittest.main()
