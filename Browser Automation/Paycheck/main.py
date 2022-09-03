import logging
from datetime import datetime


option = int(input("Option 1: Clock hours\nOption 2: Add payment\n"))
if option == 1:
    hourlyPay = 15
    #Get the date for the day worked
    format = "%m/%d/%Y"
    while True:
        try:
            date = input("Enter the date (mm/dd): ")
            date += "/2022"
            datetime.strptime(date, format)
            #print("The string is a date with format " + format)
            break
        except ValueError:
            print("The date does not have the correct format or is not a valid date")
    
    hours = input("Enter number of hours worked: ")
    logging.clock_hours(date, hours, hourlyPay, "log.txt")
elif option == 2:
    pay = input("How much has been paid?\n")
    logging.add_pay(pay, "log.txt")
else:
    print("Error: Choose an available option")

