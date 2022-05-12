from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import booking.constants as const


class Booking(webdriver.Chrome):
    def __init__(self, teardown=False):
        self.teardown = teardown
        super(Booking, self).__init__()
        self.implicitly_wait(15) #Find element methods will wait x seconds
        self.maximize_window()

    def land_first_page(self):
        self.get(const.BASE_URL)

    def __exit__(self, exc_type, exc_value, exc_traceback):
        if self.teardown:
            self.quit()

    def select_currency(self, currency=None):
        currency_button = self.find_element(By.CSS_SELECTOR, 'button[data-tooltip-text="Choose your currency"]')
        currency_button.click()

        select_currency = self.find_element(By.CSS_SELECTOR, f'a[data-modal-header-async-url-param*="selected_currency={currency}"]')
        select_currency.click()
