from datetime import datetime

def clock_hours():
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

    log = open("log.txt", "r")

    #Read the file log and store it as a list of lines in data (data[0] is the first line, total money owed)
    data = log.readlines()

    #Update the log with date and hours worked
    data.append(date + ": " + hours + " hours worked\n")
    total = int(data[0]) + int(hours) * 15
    data[0] = str(total) + "\n"
    print("New total:", total, ". Total increase is $", int(hours) * 15)
    log.close()
    #Update the total amount owed and the log dates
    log = open("log.txt", "w")
    #print(data)
    log.writelines(data)
    log.close()

def add_pay():
    pay = input("How much has been paid?\n")
    log = open("log.txt", "r")
    #Read the file log and store it in data as a list of lines
    data = log.readlines()
    #Update the log with date payed and how much is left owed
    owed = str(int(data[0]) - int(pay))
    data.append('$' + pay + " paid. Old total: " + data[0].strip() + ". New total: " + owed + "\n") #Update log with a log of the payment
    data[0] = owed + "\n" #Update the money still left owed
    log.close()
    #Update the total amount at the top of the log
    log = open("log.txt", "w")
    log.writelines(data)
    log.close()
    print('$' + pay + " has been paid")