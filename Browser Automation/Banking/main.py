from compile import Checkbook

with Checkbook(teardown=False) as bot:
    bot.land_banks()