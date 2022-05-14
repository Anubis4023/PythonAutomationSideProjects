from booking.booking import Booking

with Booking(teardown=True) as bot:
    bot.land_first_page()
    #bot.select_currency(currency='MXN')
    bot.select_destination()
    #bot.select_start_date(input('Start date? (yyyy-mm-dd)'))
    #bot.select_end_date(input('Start date? (yyyy-mm-dd)'))
    #bot.select_adults(int(input("How many adults?")))
    bot.select_start_date('2022-06-05')
    bot.select_end_date('2022-06-15')
    bot.select_adults(4)
    bot.search()
    bot.apply_filtrations()
    bot.refresh()
    bot.report()
    print("Exiting...")

    #TODO: #6 Modify to allow for user input
