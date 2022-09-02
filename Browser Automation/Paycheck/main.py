from datetime import datetime

option = int(input("Option 1: Clock hours\nOption2: Add payment"))
if option == 1:
    print("option 1")
elif option == 2:
    print("option 2")
else:
    print("Error: Choose an available option")
    
#Get the date for the day worked
format = "%m/%d/%Y"
while True:
    try:
        date = input("Enter the date (mm/dd): ")
        date += "/2022"
        datetime.strptime(date, format)
        print("The string is a date with format " + format)
        break
    except ValueError:
        print("The string is not a date with format " + format)

hours = input("Enter number of hours worked: ")

log = open("log.txt", "r")

#Read the total $
data = log.readlines()

#Update the log with date and hours worked
data.append(date + ": " + hours + " hours worked\n")
total = int(data[0]) + int(hours) * 15
data[0] = str(total) + "\n"
print("New total:", total, ". Total increase is $", int(hours) * 15)

log.close()
#Update the total amount at the top of the log
log = open("log.txt", "w")
#print(data)
log.writelines(data)
log.close()