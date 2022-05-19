from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException
from booking.filter import BookingFilter

from booking.report import BookingReport
import os
import time

#TODO: #8 make a filter class with filter functions and replace them in booking.py and refilter when a price for a hotel is retrieved in report.py

class Booking(webdriver.Chrome):
    def __init__(self, driver_path=r";C:\Users\pacow\Desktop\Selenium Drivers", teardown=False):
        self.driver_path = driver_path
        self.teardown = teardown
        os.environ['PATH'] += self.driver_path
        os.environ['PATH'] += r";C:\Users\pacow\OneDrive\Desktop\Selenium Drivers"
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        super(Booking, self).__init__(options=options)
        self.implicitly_wait(15) #Find element methods will wait x seconds
        self.maximize_window()

    def land_first_page(self):
        self.get("https://www.barcelo.com/en-us/hotels/")

    def land_second_page(self): #Before adding the volaris part, merge the branch with main because it works
        # self.get("https://www.volaris.com")
        # self.driver.switch_to.window(self.driver.window_handles[0])
        # self.driver.close()
        # self.driver.switch_to.window(self.driver.window_handles[0])
        pass

    def __exit__(self, exc_type, exc_value, exc_traceback):
        if self.teardown:
            time.sleep(3)
            self.quit()    

    def report(self, adults, rooms):
        hotels = self.find_element(By.CSS_SELECTOR, 'div[class="result__list result__list-JS"]')
        results = BookingReport(self, hotels, adults, rooms)
        results.search()
        
    def apply_filters(self):
        filter = BookingFilter(driver=self)
        filter.accept_cookies()
        filter.sort_cheapest()
        filter.choose_location()
        filter.filter_brand()
        pass
        

    

