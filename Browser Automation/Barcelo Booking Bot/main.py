from booking.booking import Booking

with Booking(teardown=False) as bot:
    bot.land_first_page()
    bot.accept_cookies()

    bot.sort_cheapest()
    bot.choose_location()
    bot.filter_brand()
    bot.report()
    

