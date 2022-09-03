import logging

option = int(input("Option 1: Clock hours\nOption 2: Add payment\n"))
if option == 1:
    logging.clock_hours()
elif option == 2:
    logging.add_pay()
else:
    print("Error: Choose an available option")

