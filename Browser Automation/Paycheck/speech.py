import speech_recognition as sr
import logging

#FIXME: #15 Script crashes when speech is not recognized, instead try to get the speech from user again

def speechInput (fileName = "NA", logFile = "log.txt"): #include an optional parameter for unit testing purposes
    hourlyPay = 15
    if fileName == "NA": #if there is no input, use microphone to get speech input
        logAgain = True
        while logAgain:
            r = sr.Recognizer()
            correct = False
            while not correct:
                with sr.Microphone() as source:
                    while True:
                        try:
                            print("Starting speech recording for date")
                            audio_data = r.record(source, duration=5)
                            print("Recognizing date")
                            #speech to text
                            text = r.recognize_google(audio_data)
                            print("Speech is:", text) #format of date heard is: mm:dd or mm dd or mmdd
                            break
                        except Exception:
                            print("Exception raised, error with speech, try again")

                    if (len(text) == 5): #mm:dd or mm dd recognized
                        month = text[0] + text[1]
                        day = text[3] + text[4]
                    elif len(text) == 4: #mmdd recognized
                        month = text[0] + text[1]
                        day = text[2] + text[3]
                    date = month + "/" + day + "/2022"

                    while True:
                        try:
                            print("Starting speech recording for hours worked")
                            audio_data = r.record(source, duration=5)
                            print("Recognizing hours")
                            hours = r.recognize_google(audio_data)
                            break
                        except Exception:
                            print("Exception raised, error with speech, try again")

                    print("Log recognized:", date, "and", hours, "hours worked")
                    print("Is this correct? Y or N\n")
                    audio_data = r.record(source, duration=5)
                    text = r.recognize_google(audio_data)
                    if text == "yes":
                        correct = True
                    elif text == "no":
                        correct = False

            logging.clock_hours(date, hours, hourlyPay, "logFile")

            with sr.Microphone() as source:
                while True:
                    try:
                        print("Continue logging hours?\n")
                        audio_data = r.record(source, duration=2)
                        text = r.recognize_google(audio_data)
                        break
                    except Exception: #If nothing is said, then treat it like user is done logging hours
                        return

                if text == "yes":
                    logAgain = True
                elif text == "no":
                    logAgain = False
    else: #Use the file given to test the speechInput function
        r = sr.Recognizer()
        with sr.AudioFile(fileName) as source:
            audio_data = r.record(source)
            text = r.recognize_google(audio_data)

            #print("Text recognized in the audio file is:", text)
            if (len(text) == 5): #mm:dd or mm dd recognized
                month = text[0] + text[1]
                day = text[3] + text[4]
            elif len(text) == 4: #mmdd recognized
                month = text[0] + text[1]
                day = text[2] + text[3]
            date = month + "/" + day + "/2022"

            with sr.AudioFile("6.wav") as src:
                audio_data = r.record(src)
                hours = r.recognize_google(audio_data)

            print("Log recognized:", date, "and", hours, "hours worked")
            logging.clock_hours(date, hours, hourlyPay, logFile)
