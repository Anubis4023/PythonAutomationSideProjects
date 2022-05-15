from booking.booking import Booking

with Booking(teardown=True) as bot:
    bot.land_first_page()
    bot.accept_cookies()
    bot.choose_location()
    bot.filter_brand()

