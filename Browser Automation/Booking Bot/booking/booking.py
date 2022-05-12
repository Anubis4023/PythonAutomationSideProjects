from selenium import webdriver
import os
import booking.constants as const


class Booking(webdriver.Chrome):
    def __init__(self):
        super(Booking, self).__init__()

    def land_first_page(self):
        self.get(const.BASE_URL)

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.quit()
    
