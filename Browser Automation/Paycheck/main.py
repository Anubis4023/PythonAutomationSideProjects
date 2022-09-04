import logging
from datetime import datetime
import speech_recognition as sr



    


option = int(input("Option 1: Clock hours\nOption 2: Add payment\n"))
if option == 1:
    hourlyPay = 15
    #Get the date for the day worked
    option = int(input("Option 1: Manual input\nOption 2: Speech input\n"))
    date = ""

    if option == 1:
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
    elif option == 2:
        r = sr.Recognizer()
        correct = False
        while not correct:
            with sr.Microphone() as source:
                print("Starting speech recording")
                audio_data = r.record(source, duration=5)
                print("Recognizing speech")
                #speech to text
                text = r.recognize_google(audio_data)
                print("Speech is:", text)

                month = text[0] + text[1]
                day = text[2] + text[3]
                hours = text[4]

                date = month + "/" + day + "/2022"
                print("Log recognized:", date, "and", hours, "hours worked")
                print("Is this correct? Y or N\n")
                audio_data = r.record(source, duration=5)
                text = r.recognize_google(audio_data)
                if text == "yes":
                    correct = True
                elif text == "no":
                    correct = False

    logging.clock_hours(date, hours, hourlyPay, "log.txt")
elif option == 2:
    pay = input("How much has been paid?\n")
    logging.add_pay(pay, "log.txt")
else:
    print("Error: Choose an available option")

