#TODO: #14 add unit testing for speech to text using audio filess
def clock_hours(date, hours, hourlyPay, fileName):
    log = open(fileName, "r")

    #Read the file log and store it as a list of lines in data (data[0] is the first line, total money owed)
    data = log.readlines()

    #Update the log with date and hours worked
    data.append(date + ": " + hours + " hours worked\n")
    total = int(data[0]) + int(hours) * hourlyPay
    data[0] = str(total) + "\n"
    print("New total:", total, ". Total increase is $", int(hours) * hourlyPay)
    log.close()
    #Update the total amount owed and the log dates
    log = open(fileName, "w")
    #print(data)
    log.writelines(data)
    log.close()

def add_pay(pay, fileName):
    log = open(fileName, "r")
    #Read the file log and store it in data as a list of lines
    data = log.readlines()
    #Update the log with date payed and how much is left owed
    owed = str(int(data[0]) - int(pay))
    data.append('$' + pay + " paid. Old total: " + data[0].strip() + ". New total: " + owed + "\n") #Update log with a log of the payment
    data[0] = owed + "\n" #Update the money still left owed
    log.close()
    #Update the total amount at the top of the log
    log = open(fileName, "w")
    log.writelines(data)
    log.close()
    print('$' + pay + " has been paid")