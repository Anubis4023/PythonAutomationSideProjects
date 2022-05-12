from booking.booking import Booking

with Booking() as bot:
    bot.land_first_page()
    #bot.select_currency(currency='MXN')
    print("Exiting...")
