from booking.booking import Booking
import time
import sys

with Booking(teardown=False) as bot:
    bot.land_first_page()
    bot.accept_cookies()

    bot.sort_cheapest()
    bot.choose_location()
    bot.filter_brand()
    #time.sleep(3) #Let page load after filters
    bot.report(int(sys.argv[1]), int(sys.argv[2]))
    #time.sleep(5)
    

