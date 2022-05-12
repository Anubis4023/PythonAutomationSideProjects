from booking.booking import Booking

with Booking(teardown=False) as bot:
    bot.land_first_page()
    bot.select_currency(currency='MXN')
    bot.select_destination()
    bot.select_start_date('2022-05-18')
    bot.select_end_date('2022-05-27')
    bot.select_adults(5)
    bot.search()
    print("Exiting...")
