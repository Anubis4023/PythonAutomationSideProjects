from selenium import webdriver
from selenium.webdriver.common.by import By
from booking.filtration import BookingFiltration
from booking.report import BookingReport
import os
import booking.constants as const
import time


class Booking(webdriver.Chrome):
    def __init__(self, driver_path=r";C:\Users\pacow\Desktop\Selenium Drivers", teardown=False):
        self.driver_path = driver_path
        self.teardown = teardown
        os.environ['PATH'] += self.driver_path
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        super(Booking, self).__init__(options=options)
        self.implicitly_wait(15) #Find element methods will wait x seconds
        self.maximize_window()

    def land_first_page(self):
        self.get(const.BASE_URL)

    def __exit__(self, exc_type, exc_value, exc_traceback):
        if self.teardown:
            #time.sleep(5)
            self.quit()

    def select_currency(self, currency=None):
        currency_button = self.find_element(By.CSS_SELECTOR, 'button[data-tooltip-text="Choose your currency"]')
        currency_button.click()

        select_currency = self.find_element(By.CSS_SELECTOR, f'a[data-modal-header-async-url-param*="selected_currency={currency}"]')
        select_currency.click()

    def select_destination(self, destination=None):
        destination_element = self.find_element(By.ID, 'ss')
        destination_element.clear()
        destination_element.send_keys('Las Vegas')
        destList_element = self.find_element(By.CSS_SELECTOR, 'li[data-i="1"]')
        destList_element.click()

    def select_start_date(self, start_date=None):
        start_date_element = self.find_element(By.CSS_SELECTOR, f'td[data-date="{start_date}"')
        start_date_element.click()

    def select_end_date(self, end_date=None):
        end_date_element = self.find_element(By.CSS_SELECTOR, f'td[data-date="{end_date}"]')
        end_date_element.click()

    def select_adults(self, numAdults=None):
        guestsMenu = self.find_element(By.ID, 'xp__guests__toggle')
        guestsMenu.click()

        numAdults_element = self.find_element(By.ID, 'group_adults')
        numAdultsText = numAdults_element.get_attribute('value')
        while int(numAdultsText) != 1:
            subAdults = self.find_element(By.CSS_SELECTOR, 'button[aria-label="Decrease number of Adults"]')
            subAdults.click()
            numAdultsText = numAdults_element.get_attribute('value')

        addAdults = self.find_element(By.CSS_SELECTOR, 'button[aria-label="Increase number of Adults"]')
        for _ in range (numAdults - 1):
            addAdults.click()

    def search(self):
        searchButton = self.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
        searchButton.click()

    def apply_filtrations (self):
        filtration = BookingFiltration(driver=self)
        #filtration.apply_star_rating(1,3,5)
        filtration.sort_price_lowest_first()
    
    def report (self):
        hotels = self.find_element(By.ID, 'search_results_table')
        results = BookingReport(hotels)
        results.get_titles()

