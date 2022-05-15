from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
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
            time.sleep(10)
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

    def filter_brand(self):
        self.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.HOME)
        time.sleep(2)

        brands = self.find_element(By.CSS_SELECTOR, 'div[data-dimension="hotel_brand"]')
        brands = brands.find_element(By.CSS_SELECTOR, 'span[class="accordion-toggle mod--icon-right"]')
        brands.click()

        barcelo = self.find_element(By.CSS_SELECTOR, 'input[name="Barceló"]')
        barcelo.click()




        #TODO: 

