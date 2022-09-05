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
        logging.clock_hours(date, hours, hourlyPay, "log.txt")
    elif option == 2:
        logAgain = True
        while logAgain:
            r = sr.Recognizer()
            correct = False
            while not correct:
                with sr.Microphone() as source:
                    print("Starting speech recording for date")
                    audio_data = r.record(source, duration=5)
                    print("Recognizing date")
                    #speech to text
                    text = r.recognize_google(audio_data)
                    print("Speech is:", text) #format of date heard is: mm:dd or mm dd or mmdd
                    
                    if (len(text) == 5): #mm:dd or mm dd recognized
                        month = text[0] + text[1]
                        day = text[3] + text[4]
                    elif len(text) == 4: #mmdd recognized
                        month = text[0] + text[1]
                        day = text[2] + text[3]
                    date = month + "/" + day + "/2022"

                    print("Starting speech recording for hours worked")
                    audio_data = r.record(source, duration=5)
                    print("Recognizing hours")
                    hours = r.recognize_google(audio_data)

                    print("Log recognized:", date, "and", hours, "hours worked")
                    print("Is this correct? Y or N\n")
                    audio_data = r.record(source, duration=5)
                    text = r.recognize_google(audio_data)
                    if text == "yes":
                        correct = True
                    elif text == "no":
                        correct = False

            logging.clock_hours(date, hours, hourlyPay, "log.txt")

            with sr.Microphone() as source:
                print("Continue logging hours?\n")
                audio_data = r.record(source, duration=2)
                text = r.recognize_google(audio_data)
                if text == "yes":
                    logAgain = True
                elif text == "no":
                    logAgain = False


elif option == 2:
    pay = input("How much has been paid?\n")
    logging.add_pay(pay, "log.txt")
else:
    print("Error: Choose an available option")

