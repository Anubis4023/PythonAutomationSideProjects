from booking.booking import Booking
import time
import sys

with Booking(teardown=False) as bot:
    #bot.land_first_page()

    # bot.apply_filters()
    # time.sleep(2)
    # bot.report(int(sys.argv[1]), int(sys.argv[2]))

    bot.land_second_page() #Open Volaris
    bot.find_tickets()
    
    

