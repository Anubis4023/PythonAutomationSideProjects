from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException

from booking.report import BookingReport
import os
import time

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

    def __exit__(self, exc_type, exc_value, exc_traceback):
        if self.teardown:
            time.sleep(3)
            self.quit()

    def accept_cookies(self):
        accept = self.find_element(By.ID, 'didomi-notice-agree-button')
        accept.click()

    def choose_location(self):
        more_button = self.find_element(By.CSS_SELECTOR, 'div[class="sidebar__facets-list"]')
        more_button = more_button.find_element(By.CSS_SELECTOR, 'div[class="facets-list__toggle-btn"]')
        more_button.click()
        
        location = self.find_element(By.CSS_SELECTOR, 'input[name="Quintana Roo"]')
        location.click()
        #time.sleep(1) #Let page load after filter

    def filter_brand(self):
        self.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)
        #time.sleep(10)

        brands = self.find_element(By.CSS_SELECTOR, 'div[data-dimension="hotel_brand"]')
        brands = brands.find_element(By.CSS_SELECTOR, 'span[class="accordion-toggle mod--icon-right"]')

        try:
            loading = self.find_element(By.CSS_SELECTOR, 'div[class="c-loading c-loading-JS bhg-loading mod--loading-active common-transition mod--fullscreen"]')
            while loading.is_displayed():
                time.sleep(1)
                print("Waited one second for loading screen")
        except:
            print("Loading screen done!")

        brands.click()

        barcelo = self.find_element(By.CSS_SELECTOR, 'input[name="Barceló"]')
        barcelo.click()
        time.sleep(1) #Let page load after filter

    def sort_cheapest(self):
        sort = self.find_element(By.ID, 'search-order')
        sort.click()

        sort_cheapest = self.find_element(By.CSS_SELECTOR, 'option[value="info.hotelLocalLowPrice"]')
        sort_cheapest.click()

        sort.click()
        time.sleep(1) #Let page load after filter

    def report(self):
        hotels = self.find_element(By.CSS_SELECTOR, 'div[class="result__list result__list-JS"]')
        results = BookingReport(self, hotels)
        results.search()
        
        

    

